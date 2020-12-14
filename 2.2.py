# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

n = 0
n = int(input('Введите количество элементов списка списка '))
my_list = []

for i in range(n):
    my_list.append(input(f'Введите элемент списка под номером {i + 1} '))

print(my_list)

# my_list = [1, 'a', 3.3, 4, (0, 1)]
count = 0

for i in range(len(my_list)):
    count += 1
    if (count % 2) != 0:
        try:
            my_list[i], my_list[i +1 ] = my_list[i + 1], my_list [i]
            # print(my_list[i], my_list[i + 1])
        except:
            None

print(my_list)