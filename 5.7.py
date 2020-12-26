# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# # название, форма собственности, выручка, издержки.
# # Пример строки файла: firm_1 ООО 10000 5000.
# # Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# # Если фирма получила убытки, в расчет средней прибыли ее не включать.
# # Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# # а также словарь со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# # Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# # Итоговый список сохранить в виде json-объекта в соответствующий файл.
# # Пример json-объекта:
# # [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# #
# # Подсказка: использовать менеджеры контекста.
from functools import reduce
import json


my_dict = {}
my_list = []

with open('5.7.txt', 'r', encoding = 'UTF-8') as f_obj:
    for line in f_obj:
        fig, revenue, costs  = '', 0, 0
        for i in line:
            if i in '1234567890':
                fig = f'{fig}{i}' #
            elif fig != '':
                if revenue == 0:
                    revenue = int(fig) #выручка
                else:
                    costs = int(fig) #издержки
                fig = ''
        if revenue - costs > 0:
            my_list.append(revenue - costs)
        l = line.find(' ') #
        my_dict[line[:l]] = revenue - costs


my_list_2 = [my_dict]

avg = round(reduce(lambda a, b: a + b, my_list) / len(my_list), 2) # я нашёл применение лямбде)))

my_list_2.append({'average_profit' : avg})

print(my_list_2)

with open('my_file.json', 'w') as write_f:
    json.dump(my_list_2, write_f)