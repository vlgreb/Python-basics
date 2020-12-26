# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

my_dict = {}

with open('f_5.3.txt', 'r', encoding = 'UTF-8') as f_obj:
    my_dict = {line.split()[0] : line.split()[1] for line in f_obj}# генерим словарь из строк файла

average_value = 0
for key, value in my_dict.items():
    if int(value) < 20000:
        print(key)
    average_value = average_value + int(value)

# print(len(my_dict))
print(f'Средняя величина дохода сотрудников = {round(average_value / len(my_dict), 2)}')
