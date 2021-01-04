# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod

class Clothes(ABC):
    @abstractmethod
    def find_consumption(self):
        pass

class Type_clothes(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @property
    def find_consumption(self):
        if self.name == 'Пальто':
            consumption = float(self.size)/6.5 + 0.5
        else:
            consumption = 2 * float(self.size) + 0.3
        return round(consumption, 2)


my_set = {'1', '2', 'q'} # выбор от пользователя

while True:
    type_of_clothes = input('Выберете тип одежды: 1 - пальто, 2 - костюм. Для выхода нажмите "q" ')
    if type_of_clothes in my_set:
        if type_of_clothes == 'q':
            break
        else:
            if type_of_clothes == '1':
                cl = 'Пальто'
                size = input(f'Введите размер {cl} ')
            else:
                cl = 'Костюм'
                size = input(f'Введите рост {cl}а ')

            clothes = Type_clothes(cl, size)
        print(clothes.find_consumption)

    else:
        print('Повторите попытку')

