# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов,
# взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

import random

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, flag=False):
    """returns n jokes of 3 words taken from 3 lists, if flag is true, returns unique jokes"""
    nouns_copy = nouns[:]
    adverbs_copy = adverbs[:]
    adjectives_copy = adjectives[:]
    result = []
    for i in range(n):
        noun = random.choice(nouns_copy)
        adverb = random.choice(adverbs_copy)
        adjective = random.choice(adjectives_copy)
        joke = f'{noun} {adverb} {adjective}'
        result.append(joke)
        if flag:
            nouns_copy.remove(noun)
            adverbs_copy.remove(adverb)
            adjectives_copy.remove(adjective)
    return result


print(get_jokes(5, flag=True))
