"""Наиболее удобный в использовании код подключения к БД."""

from collections.abc import Sequence
from json import load as jload
from mysql.connector import connect, Error as MySQLError
from pathlib import Path
from sys import path


class PersistenceManager:
    """
    Предоставляет методы для взаимодействия с БД.
    """
    default_dbconfig_path: Path | str = Path(path[0]) / 'db.json'
    default_stdout: bool = True

    @classmethod
    def _dbconfig_read(cls, dbconfig_path: Path | str = None):
        if dbconfig_path is None:
            dbconfig_path = cls.default_dbconfig_path
        with open(dbconfig_path, encoding='utf-8') as filein:
            return jload(filein)

    def __init__(self,
                 dbname: str = None,
                 dbconfig_path: Path | str = None,
                 autocommit: bool = True):
        try:
            self.connection = connect(
                **self._dbconfig_read(dbconfig_path),
                database=dbname
            )
            self.connection.autocommit = autocommit
        except MySQLError as err:
            if self.default_stdout:
                print(f'Connection failed: {err}')
        else:
            if self.default_stdout:
                print(f'Connection established')

    def select(self, query: str) -> Sequence[tuple]:
        """Возвращает данные, полученные при выполнении запроса выборки."""
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            return cursor.fetchall()

    def insert(self, query: str, ):
        """Добавляет данные в таблицу."""

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.close()

    def __del__(self):
        self.connection.close()

