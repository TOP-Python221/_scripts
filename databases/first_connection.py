"""Простой, но небезопасный и неудобный для широкого использования код подключения к БД."""

from mysql.connector import connect


connection = connect(
    host='127.0.0.1',
    port=3300,
    user='root',
    password='root',
    database='world',
)
assert connection.is_connected(), 'connection is failed'

connection.autocommit = True

cursor = connection.cursor()

select_all = """select * from country"""
# cursor.execute(select_all)
#
# columns = cursor.column_names
# print(columns)
# row = cursor.fetchone()
# print(row)
# cursor.reset()

# data = cursor.fetchall()
# for row in data:
#     print(row)
#
# cursor.execute(select_all)

create_test_db = (
    'drop schema if exists test_db; '
    'create schema test_db; '
    'use test_db; '
)
for query in create_test_db.split(';'):
    cursor.execute(query.strip())
# если autocommit выключен, то:
# connection.commit()

print(connection.database)

create_names = (
    'create table names ('
    '   id tinyint unsigned auto_increment primary key,'
    '   name char(10) not null'
    ')'
)
cursor.execute(create_names)

insert_names = (
    'insert into names'
    '   (`name`)'
    'values'
    '   (%(name_to_place)s)'
)
names_data = (
    {'name_to_place': 'Bob'},
    {'name_to_place': 'John'},
    {'name_to_place': 'Max'},
    {'name_to_place': 'George'},
)
cursor.executemany(insert_names, names_data)

cursor.execute('select * from names')
for row in cursor:
    print(row)

cursor.close()
connection.close()
