class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.show_speed()

    def go(self):
        print('Поехали')

    def stop(self):
        print('Стоп')

    def turn(self, direction):
        print('Поворот {}'.format(direction))

    def show_speed(self):
        print('Текущая скорость автомобиля {} км/ч'.format(self.speed))

    def current_car(self):
        print(f'Вы едете на {self.color} {self.name} со скоростью {self.speed} км/ч')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print('Текущая скорость автомобиля {} км/ч'.format(self.speed), '\nПревышение скорости!')
        else:
            print('Текущая скорость автомобиля {} км/ч'.format(self.speed))


class SportCar(Car):
    def sport(self):
        print('Данное авто может разгоняться до 240 км/ч')


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print('Текущая скорость автомобиля {} км/ч'.format(self.speed), '\nПревышение скорости!')
        else:
            print('Текущая скорость автомобиля {} км/ч'.format(self.speed))


class PoliceCar(Car):
    def police(self):
        if self.is_police:
            print('Вы в полицейской машине. \nможете включить сирену')


ford = TownCar(70, 'red', 'focus')
ford.current_car()
ford.turn('налево')
police = PoliceCar(90, 'white/blue', 'special', True)
police.police()
ferrari = SportCar(120, 'red', 'f40')
ferrari.go()
work = WorkCar(20, 'yellow', 'tractor')
work.current_car()
