# 1. Написать скрипт, создающий стартер (заготовку) для проекта со следующей структурой папок:
# |--my_project
#    |--settings
#    |--mainapp
#    |--adminapp
#    |--authapp
# Примечание: подумайте о ситуации, когда некоторые папки уже есть на диске (как быть?);
# как лучше хранить конфигурацию этого стартера, чтобы в будущем можно было менять имена папок под конкретный проект;
# можно ли будет при этом расширять конфигурацию и хранить данные о вложенных папках и файлах (добавлять детали)?

import os

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'уже существует!')
    else:
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(cur_dir)
