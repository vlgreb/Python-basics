class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname}')

    def get_total_income(self):
        print(f"Доход: {self._income.get('wage') + self._income.get('bonus')}")

worker_1 = Position('Иван', 'Иванов', 'Бухгалтер', {"wage": 50000, "bonus": 10000})

worker_1.get_full_name()
worker_1.get_total_income()

