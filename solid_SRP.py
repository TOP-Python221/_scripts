# SOLID -> Srp Ocp Lsp Isp Dip

"""Single Responsibility Principle — Принцип Единственной Ответственности"""

from datetime import datetime as dt
from pathlib import Path
from sys import path
from time import sleep


class Journal:
    """Для хранения текстовых записей с отметками времени."""
    def __init__(self):
        self.__entries = []

    def add_entry(self, msg: str):
        self.__entries += [(dt.now(), msg)]

    def __str__(self):
        return '\n'.join(
            f'{entry_date:%d.%m.%y %H:%M:%S} - {entry_msg}'
            for entry_date, entry_msg in self.__entries
        )

    # нарушает принцип единственной ответственности
    # def save_to_file(self):
    #     with open(Path(path[0]) / 'solid_SRP.log', 'w') as f_out:
    #         f_out.write(str(self))


# не нарушает принцип единственной ответственности
class FileSystemHandler:
    """Для работы с объектами локальной файловой системы."""
    @staticmethod
    def save_to_file(path_to_journal: Path, data: str):
        """Записывает строку в файл, перезаписывая его."""
        with open(path_to_journal, 'w') as f_out:
            f_out.write(data)



logger = Journal()
logger.add_entry('создан второй журнал')
logger.add_entry('запись для проверки 1')
sleep(2)
logger.add_entry('запись для проверки 2')
sleep(3)
logger.add_entry('ещё одна запись для проверки')
sleep(1.5)
logger.add_entry('запись для проверки 4')

# нарушает принцип единственной ответственности
# logger.save_to_file()

# не нарушает принцип единственной ответственности
FileSystemHandler.save_to_file(
    Path(path[0]) / 'solid_SRP.log',
    str(logger)
)
