# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык.
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию,
# необходимую для перевода: какой тип данных выбрать, в теле функции или снаружи.

def num_translate(number):
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
    return my_dict.get(number, None)


print(num_translate('two'))
print(num_translate('six'))
print(num_translate('sixty'))
