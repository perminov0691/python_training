# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv():
# реализовать корректную работу с числительными, начинающимися с заглавной буквы
# — результат тоже должен быть с заглавной.

def num_translate_adv(number):
    my_dict = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number.istitle():
        num_translated = my_dict.get(number.lower(), None)
        if num_translated:
            return num_translated.title()
        else:
            return 'None'
    else:
        return my_dict.get(number, None)


print(num_translate_adv('One'))
print(num_translate_adv('zero'))
print(num_translate_adv('Eight'))
print(num_translate_adv('Eleven'))
