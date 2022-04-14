# 4. Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police(булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
#
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} поехала!')

    def stop(self):
        print(f'{self.name} остановилась!')

    def turn(self, direction):
        print(f'{self.name} повернула {direction}!')

    def show_speed(self):
        print(f'текущая скорость {self.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'превышение скорости на {self.speed - 60} км/ч, текущая скорость {self.speed} км/ч')
        else:
            print(f'текущая скорость {self.speed}')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'превышение скорости на {self.speed - 40} км/ч, текущая скорость {self.speed} км/ч')
        else:
            print(f'текущая скорость {self.speed}')


class PoliceCar(Car):
    pass


sport_car = SportCar(160, 'Желтая', 'Спортивная машина', False)
town_car = TownCar(100, 'Белая', 'Городская машина', False)
work_car = WorkCar(70, 'Зеленая', 'Рабочая машина', False)
police_car = PoliceCar(250, 'Синяя', 'Полицейская машина', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
sport_car.turn('направо')
