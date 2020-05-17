total = 0
program_operation = True
while program_operation:
    numbers = input('Введите числа, разделяя их пробелом (для завершения нажмите "q"): ')
    for number in numbers.split():
        if number == 'q':
            program_operation = False
            break
        total = total + int(number)
    print('Сумма чисел = ', total)
