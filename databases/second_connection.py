"""Более безопасный и более удобный в использовании код подключения к БД."""

from collections.abc import Sequence
from json import load as jload
from mysql.connector import connect
from pathlib import Path
from sys import path


db_conn_params_path = Path(path[0]) / 'db.json'

with open(db_conn_params_path, encoding='utf-8') as filein:
    db_conn_params = jload(filein)


def select_query(query: str, db_name: str, stdout: bool = False) -> Sequence[tuple]:
    """Подключается к БД и возвращает результаты запроса выборки."""
    with connect(**db_conn_params, database=db_name) as conn:
        if stdout:
            print(f'Successful connection to {conn.server_host} as {conn.user}')
        with conn.cursor() as cur:
            cur.execute(query)
            data = cur.fetchall()
            if stdout:
                print(f'{cur.rowcount} rows was fetched')
            return data


select_all = """select * from country"""
for row in select_query(select_all, 'world', stdout=True):
    print(row)

