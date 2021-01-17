# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде
# строки формата «день-месяц-год». В рамках класса реализовать два метода. Первый, с
# декоратором @classmethod. Он должен извлекать число, месяц, год и преобразовывать их тип
# к типу «Число». Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу полученной структуры на
# реальных данных.

import datetime


class Date:
    def __init__(self, s: str):
        self.date = s

    @classmethod
    def extract(cls, param):
        cls.day = int(param[:2])
        cls.month = int(param[3:5])
        cls.year = int(param[6:10])
        return cls.day, cls.month, cls.year

    @staticmethod
    def valid(param):
        return param[1] in range(1, 12) and param[2] in range(0, 2022)


current_time = datetime.datetime.now()
date = current_time.strftime("%d/%m/%Y")

d1 = Date(date)
print(f'Текущая дата {d1.date}')
print(f'Вызов метода через название класса {Date.extract(date)}')
print(f'Вызов метода через экземпляр {d1.extract(date)}')
print(f'Валидация чисел {Date.valid(Date.extract(date))}')