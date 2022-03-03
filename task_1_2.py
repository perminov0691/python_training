# 2. Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.
numbers = []
for i in range(1, 1001, 2):
    numbers.append(i ** 3)
sum_num = 0
for num in numbers:
    sum_digits = 0
    for check_num in str(num):
        sum_digits += int(check_num)
    if sum_digits % 7 == 0:
        sum_num += num
print(sum_num)

sum_num = 0
for num in numbers:
    num += 17
    sum_digits = 0
    for check_num in str(num):
        sum_digits += int(check_num)
    if sum_digits % 7 == 0:
        sum_num += num
print(sum_num)
