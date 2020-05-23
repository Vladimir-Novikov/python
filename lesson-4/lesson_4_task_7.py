def fact(n):
    total = 1
    for num in range(1, n + 1):
        total = total * num
        yield total


x = 1
for el in fact(8):
    print(f'Факториал числа {x}! = {el}')
    x += 1
