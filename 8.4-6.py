import random


class Warehouse:
    def __init__(self, slots, max_weight):
        self.slots = slots  # количество мест хранения
        self.sl = []
        self.create_slots(slots)
        self.max_weigth = max_weight  # максимальная вместимость склада
        self._free_weigth = max_weight  # загрузка склада

    def create_slots(self, slots):
        for i in range(1, slots + 1):
            self.sl.append(Slot(i, False))

    def check_slots(self):
        print(f'Вместимость склада: {self._free_weigth}')
        for i in range(self.slots):
            print(f'Слот № {self.sl[i].id} cвободен - {self.sl[i].ind}')

    @property
    def free_weigth(self):
        return self._free_weigth

    @free_weigth.setter
    def free_weigth(self, free_weigth):
        if free_weigth < 0:
            self._free_weigth = 0
        else:
            self._free_weigth = free_weigth


class Appliances:
    def __init__(self, weigth):
        self.weight = weigth


class Printer(Appliances):
    def __init__(self, weigth):
        self.name = 'Принтер'
        super().__init__(weigth)
    @staticmethod
    def to_print():
        print('Я могу печатать')


class Scanner(Appliances):
    def __init__(self, weigth):
        self.name = 'Сканнер'
        super().__init__(weigth)
    @staticmethod
    def to_scan(self):
        print('Я могу сканировать')


class Copier(Appliances):
    def __init__(self, weigth):
        self.name = 'Копир'
        super().__init__(weigth)
    @staticmethod
    def to_copy(self):
        print('Я могу делать копии')


def create_warehouse():
    slots = random.randint(4, 8)
    max_weigth = random.randrange(500, 1000, 100)
    return Warehouse(slots, max_weigth)


def create_tech(tech):  #создание Принтера/сканнера или копира
    weigth = int(input('Введите массу '))
    return tech(weigth)


class Slot:
    def __init__(self, id, ind):
        self.id = id  #номер ячейки
        self.ind = True  # индикатор занятости ячейки

    def __str__(self):
        return f'Слот № {self.id}. Свободен - {self.ind}'

    def inside(self, tech):
        self.inside = tech
        self.include = tech.name
        self.ind = False

def write_th(th):  # функция загрузки оргтехники в ячейку
    for i in range(len(wh.sl)):
        if wh.sl[i].ind:
            wh.sl[i].inside(th)
            wh.free_weigth -= th.weight
            break
        elif i == len(wh.sl) - 1:
            print('Свободных мест для хранения нет')

wh = create_warehouse()  # создаю склад

while True:
    print('Выберете действие: 1 - создать принтер, 2 - создать сканнер, 3 - создать копир, "q" - выход')
    c = input()
    if c == 'q':
        break
    elif c == '1':
        th = create_tech(Printer)
    elif c == '2':
        th = create_tech(Scanner)
    elif c == '3':
        th = create_tech(Copier)
    else:
        print('Некорректное действие')
        continue
    write_th(th)
    wh.check_slots()
    if wh.free_weigth == 0:
        print('Склад полон')
        break
