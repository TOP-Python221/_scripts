"""Демонстратор импорта модуля из указанного файла."""

import importlib.util
import sys

from pathlib import Path

# путь к файлу с интересующим модулем
module_path = Path(sys.path[0]) / '1.py'
# имя модуля, которое будет прописано в атрибут __name__ будщего объекта модуля
module_name = 'class_model'

# создание спецификации модуля из файла с кодом
spec = importlib.util.spec_from_file_location(module_name, module_path)
# создание объекта модуля — в текущем пространстве имён он будет доступен по имени model
model = importlib.util.module_from_spec(spec)
# добавление модуля в словарь активных модулей
sys.modules[module_name] = model
# выполнение модуля
spec.loader.exec_module(model)


# пример использования:
print(model.__name__)
print('\t' + model.__doc__)

# опционально: ассоциирование объекта класса с новой переменной в текущем пространстве имён — чтобы быстрее обращаться к нужному классу
TestClass = model.A
# альтернативно: можно ранее вместо model взять более короткое имя, например ucm (university class model) 

test = TestClass()
print(f'\n{test = }\n')
test.hello()
