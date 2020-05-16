# Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

my_list = []
new_list = []
data = None
while data != 'quit':
    data = input('Вводите любые данные (для выхода из режима ввода наберите "quit"): ')
    my_list.append(data)
my_list.pop()
print(f'Вы ввели: {my_list}' if my_list else 'Список пуст, менять местами нечего')

while len(my_list) > 0:
    if len(my_list) == 1:
        new_list.append(my_list.pop(0))
        break
    new_list.append(my_list.pop(1))
    new_list.append(my_list.pop(0))

print(f'Получаем новый список с поменяными значениями: {new_list}' if new_list else 'Попробуйте ввести данные')
