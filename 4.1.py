# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv

script_name, name, work_hours, hourly_rate, bonus = argv

work_hours  = float(work_hours)
hourly_rate  = float(hourly_rate)
bonus  = float(bonus)

salary = (work_hours * hourly_rate) + bonus

print(f'Зарплата сотрудника {name} = {salary}')
