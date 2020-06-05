class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return other + self.cells

    def __sub__(self, other):
        try:
            if other - self.cells < 0:
                return 'Разность количества ячеек двух клеток меньше нуля'
            else:
                return other - self.cells
        except TypeError:
            return other - self.cells

    def __mul__(self, other):
        return other * self.cells

    def __truediv__(self, other):
        total = other / self.cells
        return round(total)

    def make_order(self, quantity):
        r = ('*' * self.cells)
        res = [''.join(r[i:i + quantity]) for i in range(0, len(r), quantity)]
        print('\n'.join(res))


cell_1 = Cell(7)
cell_2 = Cell(15)
print(f'Сложение клеток {cell_1 + cell_2}')
print(f'Вычитание клеток #1 {cell_1 - cell_2}')
print(f'Вычитание клеток #2 {cell_2 - cell_1}')
print(f'Умножение клеток {cell_1 * cell_2}')
print(f'Деление клеток #1 {cell_1 / cell_2}')
print(f'Деление клеток #2 {cell_2 / cell_1}')
cell_1.make_order(4)
print('') # добавил пустую строку для разделения двух клеток
cell_2.make_order(7)
