from pathlib import Path
from json import load, loads, dump, dumps
from pprint import pprint


# укажите путь для записи
path_dir = Path(r'')

path_read = path_dir / 'json1.json'
path_write = path_dir / 'json1_ch.json'

with path_read.open() as fh_in:
    data = load(fh_in)

# pprint(data)

for obj in data[:4]:
    obj['changed'] = False

json_changed1 = dumps(data, ensure_ascii=False)

# print(json_changed1)

data_changed2 = loads(json_changed1)

# pprint(data_changed2)

with path_write.open('w') as fh_out:
    dump(data_changed2, fh_out, ensure_ascii=False, indent=4)
