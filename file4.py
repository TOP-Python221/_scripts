from pathlib import Path

# укажите путь к каталогу с файлами
path_dir = Path()

path_file = path_dir / 'file4.txt'

text = ' '.join(str(n) for n in range(-5, 6))
with path_file.open('w') as fh_out:
    print(text, file=fh_out)
