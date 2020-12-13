# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = [7, 6, 6, 4]
print(my_list)

while True:
    el = input('Введите элемент рейтинга ')
    try:
        el = int(el)
        if el > 0:
            break
        else:
            print('Число должно быть больше 0')
    except:
        print('Вы ввели не число')

if el > my_list[0]:
    my_list.insert(0, el)
elif el < my_list[len(my_list) - 1]:
    my_list.append(el)
else:
    for i in range(len(my_list)):
        if my_list[i] < el:
            my_list.insert(i, el)


print(my_list)