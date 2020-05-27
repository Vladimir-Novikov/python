with open('lesson_5_task_5.txt', 'w+') as f:
    numbers = '\n'.join(number for number in input('Вводите числа через пробел (enter для завершения ввода): ').split())
    f.writelines(numbers)
    f.seek(0)
    value = f.readlines()
    total = 0
    for el in value:
        total = total + float(el)
print('Сумма чисел:', total)
