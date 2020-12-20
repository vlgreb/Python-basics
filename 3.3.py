# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.sort()
    my_list.reverse()
    return my_list[0] + my_list[1]

a, b, c = 30, 0.5, 10

print(my_func(a, b, c))