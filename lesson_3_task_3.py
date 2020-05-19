def my_func(a, b, c):
    numbers = [a, b, c]
    numbers.remove(min(numbers))
    return sum(numbers)


num_1 = int(input('Введите число a: '))
num_2 = int(input('Введите число b: '))
num_3 = int(input('Введите число c: '))
result = my_func(num_1, num_2, num_3)
print('Сумма наибольших двух элементов ', result)
