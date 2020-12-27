# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

with open('f_5.5.txt', 'w', encoding = 'UTF-8') as f_obj:
    for i in range(10):
        f_obj.write(f'{str(random.randint(0, 10))} ')
    f_obj.seek(0)

f_obj = open('f_5.5.txt', 'r', encoding = 'UTF-8')
my_str = f_obj.readline()
f_obj.close()
print(my_str)

my_list = my_str.split()
sum = 0
for el in my_list:
    sum = sum + int(el)

print(sum)



