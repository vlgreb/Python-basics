# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police=bool ):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        print('Машина поехала')
    def stop(self):
        print('Машина остановилась')
    def turn(self, side):
        print(f'Машина повернула в {side}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    pass

class SportCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print(f'У машины {self.name} превышение скорости!')


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print(f'У машины {self.name} превышение скорости!')


class PoliceCar(Car):
    def check_police(self):
        print(f'Маниша {self.name} полицейская - {self.is_police}')

car_1 = TownCar('Лада', '50', 'Баклажан', False)
print(car_1.color)

car_2 = SportCar('Тойота', '100', 'Черный', False)
car_2.show_speed()

car_3 = WorkCar('Рено', '50', 'Белый', False)
car_3.show_speed()


car_4 = PoliceCar('Форд', '50', 'Бело-синий', True)
car_4.check_police()