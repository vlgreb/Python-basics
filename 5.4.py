# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

f_ru = open('f_5.4_ru.txt', 'w', encoding = 'UTF-8')

with open('f_5.4_en.txt', 'r', encoding = 'UTF-8') as f_en_obj:
    for line in f_en_obj:
        s = line.replace('One', 'Один').replace('Two','Два').replace('Three','Три').replace('Four','Четыре')
        f_ru.write(f'{s}')


f_ru.close()

# print(dict.keys())
# print(dict[my_dict.values('1')])
# with open('f_5.4_rus.txt', 'a') as f_rus_obf:
