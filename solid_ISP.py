"""Interface Segregation Principle — Принцип Разделения Интерфейсов."""

# интерфейс, нарушающий принцип разделения интерфейсов
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

    # не используемые методы по-прежнему присутствуют в области видимости
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

    # не используемые методы по-прежнему присутствуют в области видимости
    def fax(self):
        raise NotImplementedError('обмен данными по факсу невозможен')


brother_hl5250dn = Printer()
brother_hl5250dn.print()
# brother_hl5250dn.fax()



# разделённые интерфейсы
class IPrinter:
    def print(self):
        print('использование протокола печати')

class IScanner:
    def scan(self):
        print('использование протокола сканирования')

class IFax:
    def fax(self):
        print('использование протокола обмена данными по факсу')


class Fax(IFax):
    def fax(self):
        super().fax()
        print('отправка факса, получение факса')


class MFD(IPrinter, IScanner, IFax):
    def print(self):
        super().print()
        print('печать страницы')

    def scan(self):
        super().scan()
        print('сканирование страницы')

    def fax(self):
        super().fax()
        print('отправка факса, получение факса')


hp_660 = MFD()
hp_660.scan()

sony_fm_10 = Fax()
sony_fm_10.fax()
# sony_fm_10.print()
