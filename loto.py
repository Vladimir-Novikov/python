import random
from time import time


class Cards:
    """ В методе make_card формируем карточки по 5 цифр в строке, 3 строки.
    Оставшиеся места (4) заполняем в рандомном порядке пропусками.
    Метод print_card вызываем при каждом новом бочонке. В init запускаем таймер."""
    def __init__(self):
        self.start = time()
        self.user = []
        self.pc = []
        self.make_card(self.user)
        self.make_card(self.pc)

    def make_card(self, name):
        lines = 0
        while lines < 3:
            line = []
            while len(line) < 5:
                rand_num = (random.randint(1, 90))
                if line.count(rand_num) == 1 or name.count(rand_num) == 1:
                    continue
                line.append(rand_num)
            line.sort()
            for p in range(4):
                rand_passes = random.randint(1, 9)
                line.insert(rand_passes, 0)
            name += line
            lines += 1

    def print_card(self, name):
        if name == self.user:
            print('____Карточка игрока____')
        else:
            print('__Карточка компьютера__')
        for num, replacing_el in enumerate(name):
            if num == 9 or num == 18:
                print('')
            if replacing_el == 0:
                print(' ', end='')
            else:
                print(replacing_el, end=' ')
        print('')
        print('_______________________')


make = Cards()


class Barrel:
    """Достаем бочонок из мешка. Если рандомное число уже было (field), то повторяем."""
    def __init__(self):
        self.field = []

    def next_barrel(self):
        while len(self.field) < 90:
            n = (random.randint(1, 90))
            if self.field.count(n) == 1:
                continue
            self.field.append(n)
            return n


bar = Barrel()


class UserMove:
    """Получаем действие пользователя (зачеркнуть или нет)"""
    @staticmethod
    def user_move():
        while True:
            answer = input('Зачеркнуть цифру? (y/n) ').lower()
            if answer == 'y' or answer == 'n':
                break
            print('Ответ может быть только y или n')
        return answer


class EndGame:
    """Проверка на наличие в карточке цифр или уже все зачеркнуто. Выводим кто победил.
    Получаем время окончания игры."""
    @staticmethod
    def end_game():
        if make.pc.count('-') == 15 and make.user.count('-') == 15:
            finish = time()
            print('*** Редкий случай: ничья ***\n Игра заняла {} секунд'.format(round(finish - make.start)))
            return False
        elif make.pc.count('-') == 15:
            finish = time()
            print('*** Победил компьютер за {} секунд ***'.format(round(finish - make.start)))
            return False
        elif make.user.count('-') == 15:
            finish = time()
            print('*** Победил игрок, это заняло {} секунд ***'.format(round(finish - make.start)))
            return False
        else:
            return True

    @staticmethod
    def stop():
        print('Это не правильный вариант\nВы проиграли!')


class Comparison:
    """Сравнение овета пользователя. Если число есть и пользователь ответил Y то вычеркиваем это число.
    Поиск идет по индексу, потом pop и insert.
    Если пользователь ошибся, то завершение игры.
    Здесь же вызываем печать карточек.
    В карточке ПК цифры вычеркиваются автоматичести, т.к. ПК не ошибается."""
    @staticmethod
    def comparison():
        while EndGame.end_game():
            n = bar.next_barrel()
            print(f'Новый бочонок: {n} (осталось {90 - len(bar.field)})')
            if make.pc.count(n) == 1:
                ind = (make.pc.index(n))
                make.pc.pop(ind)
                make.pc.insert(ind, '-')
            make.print_card(make.user)
            make.print_card(make.pc)
            user = UserMove.user_move()
            if make.user.count(n) == 1 and user == 'y':
                ind = (make.user.index(n))
                make.user.pop(ind)
                make.user.insert(ind, '-')
            elif make.user.count(n) == 1 and user == 'n':
                EndGame.stop()
                break
            elif make.user.count(n) == 0 and user == 'y':
                EndGame.stop()
                break


Comparison.comparison()
