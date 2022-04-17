# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# | 31 22 |
# | 37 43 |
# | 51 86 |
#
# | 3 5 32 |
# | 2 4 6 |
# | -1 64 -8 |
#
# | 3 5 8 3 |
# | 8 3 7 1 |
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и пр.

class Matrix:
    def __init__(self, input_data):
        self.input = input_data

    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.input])

    def __add__(self, other):
        result = ''
        if len(self.input) == len(other.input):
            for line1, line2 in zip(self.input, other.input):
                if len(line1) != len(line2):
                    return 'problems with shape'
                else:
                    summed_line = [x + y for x, y in zip(line1, line2)]
                    result += ' '.join(map(str, summed_line)) + '\n'
        else:
            return 'problems with shape'
        return result


matrix_1 = Matrix([[1, 2], [3, 4], [5, 6], [7, 8]])
matrix_2 = Matrix([[9, 10], [11, 12], [13, 14], [15, 16]])
print(matrix_1)
print(matrix_1 + matrix_2)
