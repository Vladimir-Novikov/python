wage_ron = {'wage': 5000, 'bonus': 1000}
wage_mick = {'wage': 9000, 'bonus': 3000}

class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        full_name = f'{self.name} {self.surname}'
        print(full_name)

    def get_total_income(self):
        total = self._income['wage'] + self._income['bonus']
        print(total)


employee_1 = Position('Ron', 'Black', 'intern', wage_ron)
employee_1.get_full_name()
print(employee_1.position)
employee_1.get_total_income()
employee_2 = Position('Mick', 'White', 'driver', wage_mick)
employee_2.get_full_name()
employee_2.get_total_income()
