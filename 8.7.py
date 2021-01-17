# 7. Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа)
# и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'{self.a}+{self.b}i'

    def __add__(self, other):
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        return Complex(self.a*other.a - self.b*other.b, self.b*other.a + self.a*other.b)

c1 = Complex(2, 3)
c2 = Complex(5, 6)
c3 = c1 + c2
c4 = c1*c2
print(c1, c2)
print(f'Результат сложения: {c3}')
print(f'Результат умножения: {c4}')