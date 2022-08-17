import os


path_dir = 'c:\\Windows'

path_dir = r'c:\Windows'

path_file1 = r'\DPINST.LOG'
path_file2 = r'\BRWMARK.INI'

fh_in = open(path_dir+path_file1, encoding='utf-16')
print(f"{type(fh_in) = }\n")
print(f"{fh_in = }\n")
print(f"{fh_in.read() = }\n\n")
fh_in.close()

fh_in = open(path_dir+path_file2, encoding='ansi')
print(f"{type(fh_in) = }\n")
print(f"{fh_in = }\n")
print(f"{fh_in.read() = }\n\n")
fh_in.close()

