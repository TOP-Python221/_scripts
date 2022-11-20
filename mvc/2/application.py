"""Приложение с интерфейсом командной строки (CLI) для работы с товарной базой магазина."""
from typing import Type

import storage_operations as so


class Model:
    """
    
    """
    def __init__(self, items: list[dict] = None):
        self._item_type = 'ПРОДУКТЫ ПИТАНИЯ'
        if items is not None:
            self.create_items(items)

    @property
    def item_type(self) -> str:
        """Тип товарной позиции."""
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type: str):
        """Изменение типа товарной позиции."""
        self._item_type = new_item_type

    @staticmethod
    def create_items(items_list: list[dict]):
        """Добавляет несколько позиций в товарную базу."""
        return so.create_items(items_list)

    @staticmethod
    def create_item(name: str, price: str, quantity: int):
        """Добавляет одну позицию в товарную базу."""
        return so.create_item(name, price, quantity)

    @staticmethod
    def read_items() -> list[dict]:
        """Возвращает все позиции из товарной базы."""
        return so.read_items()

    @staticmethod
    def read_item(name: str) -> dict:
        """Возвращает одну позицию из товарной базы."""
        return so.read_item(name)

    @staticmethod
    def update_item(name: str, /, *, new_price: str = None, new_quantity: int = None):
        """Обновляет поля 'цена' и/или 'количество' для одной позиции из товарной базы."""
        return so.update_item(name, price=new_price, quantity=new_quantity)

    @staticmethod
    def delete_item(name: str):
        """Удаляет одну позицию из товарной базы."""
        return so.delete_item(name)


class View:
    """
    Представление для вывода в стандартный поток информации об операциях с товарной базой.
    """
    @staticmethod
    def show_bullet_point_list(item_type: str, items: list):
        print(f'--- {item_type} ---')
        for item in items:
            print(f'* {item}')

    @staticmethod
    def show_number_point_list(item_type: str, items: list):
        print(f'--- {item_type} ---')
        for i, item in enumerate(items):
            print(f'{i+1}. {item}')

    @staticmethod
    def show_item(item_type: str, item_name: str, item_info: dict):
        print('//////////////////////////////////////////////////////////////')
        print(f'Good news, we have some {item_name}!')
        print(f'{item_type} INFO: {item_info}')
        print('//////////////////////////////////////////////////////////////')

    @staticmethod
    def display_missing_item_error(item_name: str, err_msg: str):
        print('**************************************************************')
        print(f'We are sorry, we have no {item_name}!')
        print(f'{err_msg}')
        print('**************************************************************')

    @staticmethod
    def display_item_already_stored_error(item_type: str, item_name: str, err_msg: str):
        print('**************************************************************')
        print(f'Hey! We already have {item_name} in our {item_type} list!')
        print(f'{err_msg}')
        print('**************************************************************')

    @staticmethod
    def display_item_not_yet_stored_error(item_type: str, item_name: str, err_msg: str):
        print('**************************************************************')
        print(f'We don\'t have any {item_name} in our {item_type} list. Please insert it first!')
        print(f'{err_msg}')
        print('**************************************************************')

    @staticmethod
    def display_item_stored(item_type: str, item_name: str):
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        print(f'Hooray! We have just added some {item_name} to our {item_type} list!')
        print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')

    @staticmethod
    def display_change_item_type(older_item_type: str, newer_item_type: str):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change item type from "{older_item_type}" to "{newer_item_type}"')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_updated(item_name: str,
                             o_price: str, o_quantity: int,
                             n_price: str, n_quantity: int):
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')
        print(f'Change {item_name} price: {o_price} --> {n_price}')
        print(f'Change {item_name} quantity: {o_quantity} --> {n_quantity}')
        print('---   ---   ---   ---   ---   ---   ---   ---   ---   ---   --')

    @staticmethod
    def display_item_deletion(item_name: str):
        print('--------------------------------------------------------------')
        print(f'We have just removed {item_name} from our list')
        print('--------------------------------------------------------------')


class Controller:
    """

    """
    def __init__(self, model_cls: Type, view_obj: View):
        self.__ModelCls = model_cls
        self.model = None
        self.view = view_obj

    def start(self, items: list[dict] = None):
        self.model = self.__ModelCls(items)

    def show_items(self, numbered_list: bool = False):
        data = self.model.read_items()
        if numbered_list:
            self.view.show_number_point_list(self.model.item_type,
                                             data)
        else:
            self.view.show_bullet_point_list(self.model.item_type,
                                             data)

    def show_item(self, name: str):
        try:
            data = self.model.read_item(name)
            self.view.show_item(self.model.item_type,
                                name,
                                data)
        except so.ItemNotStoredError as e:
            self.view.display_item_not_yet_stored_error(
                self.model.item_type,
                name,
                str(e)
            )

    def insert_item(self, name: str, price: str, quantity: int):
        try:
            self.model.create_item(name, price, quantity)
            self.view.display_item_stored(self.model.item_type,
                                          name)
        except so.ItemAlreadyStoredError as e:
            self.view.display_item_already_stored_error(
                self.model.item_type,
                name,
                str(e)
            )

    def update_item(self,
                    name: str,
                    /, *,
                    new_price: str = None,
                    new_quantity: int = None):
        try:
            data = self.model.read_item(name)
            self.model.update_item(name,
                                   new_price=new_price,
                                   new_quantity=new_quantity)
            self.view.display_item_updated(
                name,
                data['price'],
                data['quantity'],
                new_price if new_price is not None else data['price'],
                new_quantity if new_quantity is not None else data['quantity']
            )
        except so.ItemNotStoredError as e:
            self.view.display_item_not_yet_stored_error(
                self.model.item_type,
                name,
                str(e)
            )

    def delete_item(self, name: str):
        try:
            self.model.delete_item(name)
            self.view.display_item_deletion(name)
        except so.ItemNotStoredError as e:
            self.view.display_item_not_yet_stored_error(
                self.model.item_type,
                name,
                str(e)
            )


# тесты
if __name__ == '__main__':

    goods = [
        {'name': 'Хлеб', 'price': '36.22', 'quantity': 8},
        {'name': 'Молоко', 'price': '91.80', 'quantity': 11},
        {'name': 'Шоколад', 'price': '158.00', 'quantity': 5},
    ]

    app = Controller(Model, View())
    app.start(goods)

    app.show_items()
    print()

    app.show_items(True)
    print()

    app.show_item('Пиво')
    print()

    app.insert_item('Пиво', '75.00', 20)
    print()

    app.show_item('Пиво')
    print()

    app.insert_item('Хлеб', '75.00', 20)
    print()

    app.update_item('Пиво', new_quantity=16)
    print()

    app.delete_item('Шоколад')
    print()
