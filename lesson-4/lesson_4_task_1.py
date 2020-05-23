from sys import argv


def wages(hours, rate, bonus):
    total = int(hours) * int(rate) + int(bonus)
    print(f'Отработано {hours} часов')
    print(f'Ставка {rate} руб/час')
    print(f'Премия {bonus} руб')
    print(f'Заработная плата сотрудника составила: {total} руб')


hours = argv[1]
rate = argv[2]
bonus = argv[3]
wages(hours, rate, bonus)
