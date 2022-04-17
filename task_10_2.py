# 2. Реализовать проект расчёта суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определённое название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма(2*H + 0.3). Проверить работу этих методов на реальных данных.
# Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке знания.
# Реализовать абстрактные классы для основных классов проекта и проверить работу декоратора @property.
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def consumption(self):
        pass

    def __str__(self):
        return str(self.param)


class Coat(Clothes):

    @property
    def consumption(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):

    @property
    def consumption(self):
        return self.param * 2 + 0.3


coat = Coat(70)
suit = Suit(46)
print(coat)
print(suit)
print(coat.consumption)
print(suit.consumption)
