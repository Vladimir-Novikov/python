def my_func(x, y):
    return x ** y


def my_func_2(x, y):
    divider = 1
    if y < 0:
        while y < 0:
            divider = divider * x
            y += 1
        result = 1 / divider
        return result
    else:
        while y > 0:
            divider = divider * x
            y -= 1
        return divider


num_1 = int(input('Введите действительное положительное число x: '))
num_2 = int(input('Введите целое отрицательное число y: '))

print('Решение через **: ', my_func(num_1, num_2))
print('Решение через цикл while', my_func_2(num_1, num_2))
