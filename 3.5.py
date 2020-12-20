# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# # При нажатии Enter должна выводиться сумма чисел.
# # Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# # Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# # Но если вместо числа вводится специальный символ, выполнение программы завершается.
# # Если специальный символ введен после нескольких чисел,
# # то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def check_func(check_list): #функция проверки корректности ввода чисел пользователем
    for i in range(len(check_list)):
        try:
            check_el = float(check_list[i])
            # print(check_el)
        except:
            if (i == len(check_list) - 1) and (check_list[i] == 'q'):
                return True
            else:
                return False
    return True

def sum_func(sum_list):
    sum = 0
    for i in range(len(sum_list)):
        if sum_list[i] != 'q':
            sum += float(sum_list[i])
    return sum



my_str = ''
print('Введите стоку чисел, разделённых пробелом (для выхода введите "q") ')
sum_ = 0

while True:
    # my_str = input('Введите стоку чисел, разделённых пробелом (для выхода введите "q") ')
    if sum_ == 0:
        my_str = input()
    else:
        my_str = f'{sum_} {input()}'

    my_list = my_str.split()
    # print(my_list)

    if check_func(my_list):
        sum_ = sum_func(my_list)
        print(sum_, end = ' ')
    else:
        print('Вы ввели не числа. Попробуйте ещё раз')
        continue

    if my_list[len(my_list) - 1] == 'q':
        break

