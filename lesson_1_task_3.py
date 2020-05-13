# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = (input('Введите число: '))
number_2 = number * 2
number_3 = number * 3
total = int(number) + int(number_2) + int(number_3)
print(total)
