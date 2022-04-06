# 3. Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике).
# Написать скрипт, который собирает все шаблоны в одну папку templates, например:
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html

import os
import shutil

my_dir = 'templates'
if not os.path.exists(my_dir):
    os.mkdir(my_dir)

folder = r'my_project'
files = []

for r, d, f in os.walk(folder):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    new_folder = os.path.join(my_dir, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(new_folder):
        os.mkdir(new_folder)
    save_path = os.path.join(new_folder, os.path.basename(path))
    shutil.copy(path, save_path)
