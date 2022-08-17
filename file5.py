from pathlib import Path
from pprint import pprint

# укажите путь к каталогу с файлами
path_dir = Path()

path_file = path_dir / 'poker.py'

lines = tuple()
with path_file.open() as fh_in:
    while line := fh_in.readline():
        lines += (line,)
pprint(lines)
print('\n\n')


path_file = path_dir / 'matrix.py'
def gen_readline(path):
    with open(path) as fh_in:
        while line := fh_in.readline():
            yield line

grlm = gen_readline(path_file)
while True:
    try:
        print(next(grlm), end='')
    except StopIteration:
        print(f'\n\t___конец файла {path_file.name}')
        break
