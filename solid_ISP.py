"""Interface Segregation Principle — Принцип Разделения Интерфейсов."""

class MultiFunctionDevice:
    def print(self):
        print('использование протокола печати')

    def scan(self):
        print('использование протокола сканирования')

    def fax(self):
        print('использование протокола обмена данными по факсу')


class Printer(MultiFunctionDevice):
    """Классический принтер."""
    def print(self):
        super().print()
        print('печать страницы')

    def scan(self):
        raise NotImplementedError('сканирование невозможно')

    def fax(self):
        raise NotImplementedError('обмен данными по факсу невозможен')


class Xerox(MultiFunctionDevice):
    def print(self):
        super().print()
        print('печать страницы')

    def scan(self):
        super().scan()
        print('сканирование страницы')

    def fax(self):
        raise NotImplementedError('обмен данными по факсу невозможен')



brother_hl5250dn = Printer()
brother_hl5250dn.print()
brother_hl5250dn.fax()
