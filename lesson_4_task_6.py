from itertools import count, cycle

start = 0
finish = 0

number = False
while not number:
    user_number = (input('Введите через пробел с какого числа начинать отсчет и каким завершать: ')).split()
    for el in user_number:
        try:
            start = int(user_number[0])
            finish = int(user_number[1])
        except IndexError:
            print('** Необходимо 2 числа **')
            break
        except ValueError:
            print('** Нужно вводить числа! **')
            break
        else:
            if finish < start:
                print('** Первое число должно быть меньше второго **')
                break
        number = True

for i in count(start):
    print(i)
    if i == finish:
        break

user_text = input('А теперь введите текст. Программа повторит его элементы 30 раз: ')
i = 1
for el in cycle(user_text):
    print(el)
    if i == 30:
        break
    i += 1
