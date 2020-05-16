# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

while True:
    try:
        user_data = int(input('Введите месяц (число от 1 до 12): '))
        if user_data > 12 or user_data < 1:
            print('Введены некорректные данные!')
        else:
            break
    except ValueError:
        print('Нужно ввести число')

month = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
season = ['зима', 'весна', 'лето', 'осень']

print('Вы выбрали месяц', month[user_data - 1])

if 11 >= user_data >= 9:
    print('Это', season[3])
elif 5 >= user_data >= 3:
    print('Это', season[1])
elif 8 >= user_data >= 6:
    print('Это', season[2])
else:
    print('Это', season[0])
