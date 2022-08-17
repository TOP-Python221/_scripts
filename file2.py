from pathlib import Path

# укажите путь к каталогу с файлами
path_dir = Path()

path_file1 = path_dir / 'file1_1.txt'
path_file2 = path_dir / 'file1_2.txt'

with path_file1.open() as fh_in:
    print(f"{type(fh_in)}")
    print(f"{fh_in.read()}")

with path_file2.open(encoding='866') as fh_in:
    text = fh_in.read()

print(text)

text.split()
