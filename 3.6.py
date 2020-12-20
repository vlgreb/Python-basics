# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре.
# Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы.
# Необходимо использовать написанную ранее функцию int_func()

def check_str(str_check): #функция проверки корректности ввода
    for i in range(len(str_check)):
        if str_check[i] not in 'abcdefghijklmnopqrstuvwxyz ':
            return False
    return True

def int_func(str_in):
    str_out = str_in[0].upper()
    for i in range(1, len(str_in)):
        str_out = str_out + str_in[i]
    # str_def[0] = str_def[0].upper()
    return(str_out)


while True:
    my_str = input('Введите строку из маленьких латинских букв ')
    if check_str(my_str) == False:
        print('Попробуйте ещё разок')
    else:
        break

my_list = my_str.split()

ex_str = ''
for i in range(len(my_list)):
    ex_str = f'{ex_str} {int_func(my_list[i])}'
print(ex_str)
# print(int_func(input()))
