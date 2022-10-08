
class CPU:
    """Моделирует работу центрального процессора."""
    @staticmethod
    def start_cooling():
        print('CPU is cooling')

    @staticmethod
    def read_register(register: str):
        print(f'CPU is reading register {register}')

    @staticmethod
    def execute():
        print('CPU is starting')


class RAM:
    """Моделирует работу оперативной памяти."""
    @staticmethod
    def load(data: str) -> str:
        print(f'RAM is reading data: {data}')
        return ''.join(bin(ord(ch))[2:] for ch in data)


class Drive:
    """Моделирует работу носителя данных."""
    @staticmethod
    def read_block(block_address: str) -> str:
        print(f'Drive is reading block of data from {block_address}')
        return ''.join(hex(ord(ch))[2:] for ch in block_address).upper()


class Computer:
    """Обеспечивает возможность запуска компьютера.

    Фасад для компонентов компьютера.
    """
    def __init__(self):
        self.cpu = CPU()
        self.ram = RAM()
        self.drive = Drive()

    def start(self):
        self.cpu.start_cooling()
        self.cpu.execute()
        mbr = self.drive.read_block('00001200')
        print(mbr)
        mbr = self.ram.load(mbr)
        print(mbr)
        self.cpu.read_register(mbr)


pc = Computer()
pc.start()
