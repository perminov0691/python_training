# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи,
# в которых фамилия начинается с соответствующей буквы. Например:
# >>> thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "И": {
#         "И": ["Илья Иванов"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }

def thesaurus_adv(*names_and_surnames):
    names_and_surnames_dict = {}
    for el in names_and_surnames:
        surname = el.split()[1]
        key_1 = surname[0].capitalize()
        if key_1 not in names_and_surnames_dict:
            names_dict = {}
            names_and_surnames_dict[key_1] = names_dict
            for element in names_and_surnames:
                surname_2 = element.split()[1]
                name = element.split()[0]
                if surname_2[0] == key_1:
                    key_2 = name[0].capitalize()
                    if key_2 not in names_dict:
                        names_dict[key_2] = []
                    names_dict[key_2].append(element)
    return names_and_surnames_dict


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"))
