first = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
second = [el for el in first if first.count(el) == 1]
print(f'Исходный список {first}')
print(f'Итоговый список {second}')
