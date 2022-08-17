from pathlib import Path

# укажите путь к каталогу с файлами
path_dir = Path()

path_file1 = path_dir / 'file3_1.txt'
path_file2 = path_dir / 'file3_2.txt'


text_out1 = '\n'.join(str(n) for n in range(-10, 11)) + '\n'
text_out2 = ','.join(str(n) for n in range(-10, 11)) + '\n'
text_out3 = ','.join(str(n) for n in range(100, 115)) + '\n'

# если файла не существует, то он будет создан
with path_file1.open('w') as fh_out:
    fh_out.write(text_out1)

# полностью перезаписывает содержимое файла
with path_file1.open('w') as fh_out:
    fh_out.write(text_out2)


# если файла не существует, то он будет создан
with path_file2.open('a') as fh_out:
    chars_num = fh_out.write(text_out2)
print(f"Записано {chars_num} символов")

# дописывает в конец файла
with path_file2.open('a') as fh_out:
    chars_num = fh_out.write(text_out3)
print(f"Записано {chars_num} символов")
