# Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input('Введите целое положитетельное число: '))
divider = 10
max_number = number % 10
while divider < number * 10:
    next_number = (number // divider) % 10
    if next_number > max_number:
        max_number = next_number
    divider *= 10
print('Самая большая цифра в числе:', max_number)
