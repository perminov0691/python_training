# 3.Склонение слова
# Реализовать склонение слова «процент» во фразе «N процентов».
# Вывести эту фразу на экран отдельной строкой для каждого из чисел в интервале от 1 до 100:
# 1 процент
# 2 процента
# 3 процента
# 4 процента
# 5 процентов
# 6 процентов
# ...
# 100 процентов

for i in range(1, 101):
    if i == 1 or (i > 20 and i % 10 == 1):
        print(i, 'процент')
    elif i == 2 or i == 3 or i == 4 or (i > 20 and i % 10 == 2) or (i > 20 and i % 10 == 3) or (i > 20 and i % 10 == 4):
        print(i, 'процента')
    else:
        print(i, 'процентов')