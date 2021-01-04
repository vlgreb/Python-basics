class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        sub_cells = int(self.cells) - int(other.cells)
        if sub_cells > 0:
            return sub_cells
        else:
            return 'Вычитание клеток невозможно'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(int(self.cells / other.cells))

    def make_order(self, num):
        my_str = ''
        for i in range(self.cells // num):
            my_str = f'{my_str}{"*"*num}\n'
        my_str = f'{my_str}{"*"*(self.cells % num)}.'
        return my_str


def check_input(check_str):
    if check_str in '123456789q':
        return True
    else:
        return False


def create_cell():
    while True:
        my_str = input('Создаём клетку. Введите количество ячеек от 1 до 9. Для выхода нажмите "q" ')
        if check_input(my_str):
            if my_str == "q":
                return None
            else:
                return Cell(int(my_str))
        else:
            print('Повторите попытку')


while True:
    c1 = create_cell()
    if c1 is None:
        break
    c2 = create_cell()
    if c2 is None:
        break
    c3 = c1 + c2
    print(f'Сложение клеток {c3.cells}')
    c4 = c1 - c2
    print(f'Вычитание клеток {c4}')
    c5 = c1 * c2
    print(f'Умножение клеток {c5.cells}')
    c6 = c1 / c2
    print(f'Деление клеток {c6.cells}')
    print(c1.make_order(int(input('Введите количество ячеек в ряду для первой клетки '))))
