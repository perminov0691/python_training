# 5. * (вместо 4) Написать скрипт, который выводит статистику для заданной папки в виде словаря,
# в котором ключи те же, а значения — кортежи вида (<files_quantity>, [<files_extensions_list>]), например:
#   {
#       100: (15, ['txt']),
#       1000: (3, ['py', 'txt']),
#       10000: (7, ['html', 'css']),
#       100000: (2, ['png', 'jpg'])
#     }
# Сохраните результаты в файл <folder_name>_summary.json в той же папке, где запустили скрипт.

import os
import json

files = []
for r, d, f in os.walk('./'):
    for file in f:
        file_path = os.path.join(r, file)
        files.append((file_path.split('.')[-1], os.stat(file_path).st_size))
max_size = max(files, key=lambda x: x[1])[1]

i = 1
out_dict = {}

for _ in range(len(str(max_size))):
    i *= 10
    out_dict[i] = (0, [])

for file in files:
    num, ext_list = out_dict[10 ** len(str(file[1]))]
    ext_list.append(file[0])
    ext_list = list(set(ext_list))
    out_dict[10 ** len(str(file[1]))] = (num + 1, ext_list)

print(out_dict)

with open(os.path.basename(os.getcwd()) + '_summary.json', 'w') as f:
    json.dump(out_dict, f)
