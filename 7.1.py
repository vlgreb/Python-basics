# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.
import random

class Matrix:
    matrix = []
    def __init__(self, name = 'Матрица'):
        self.matrix = []
        self.name = name
        for i in range(5):
            self.matrix.append([random.randint(0, 9) for el in range(5)])

    def __str__(self):
        my_str = ''
        for i in range(5):
            for j in range(5):
                my_str = f'{my_str} {self.matrix[i][j]}'
            my_str = f'{my_str}\n'
        return my_str

    def __add__(self, other):
        m = Matrix()
        for i in range(5):
            for j in range(5):
                m.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return m


m1 = Matrix('Матрица А')
print(m1.name, '\n', m1)

m2 = Matrix('Матрица Б')
print(m2.name, '\n', m2)

m3 = m1 + m2
print(m3)