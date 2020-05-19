def division(a, b):
    try:
        return a / b, b / a
    except ZeroDivisionError:
        print('На 0 делить нельзя!')


num_a = float(input('Введите число a: '))
num_b = float(input('Введите число b: '))
try:
    answer_1, answer_2 = division(num_a, num_b)
    print(f'Деление {num_a} на {num_b} = {answer_1}\nДеление {num_b} на {num_a} = {answer_2}')
except TypeError:
    print('Попробуйте еще раз')
