# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников
# и возвращающую словарь, в котором ключи — первые буквы имён, а значения — списки,
# содержащие имена, начинающиеся с соответствующей буквы.

def thesaurus(*names):
    names_dict = {}
    for name in names:
        key = name[0].capitalize()
        if key not in names_dict:
            names_dict[key] = []
        names_dict[key].append(name)
    return names_dict


print(thesaurus("Иван", "Мария", "Петр", "Илья"))
