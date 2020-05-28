class Stationery:
    def __init__(self, title):
        self.title = title
        self.draw()

    def draw(self):
        print(self.title, '\nЗапуск отрисовки')


class Pen(Stationery):

    def draw(self):
        print(f'{self.title}. Рисуем ручкой')


class Pencil(Stationery):
    def draw(self):
        print(f'{self.title}. Рисуем карандашом')


class Handle(Stationery):
    def draw(self):
        print(f'{self.title}. Рисуем маркером')


start = Stationery('Начинаем')
pen = Pen('Шариковая ручка')
pencil = Pencil('Простой карандаш')
handle = Handle('Перманентный маркер')
