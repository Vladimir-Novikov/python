# Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

list_of_data = ['text', 123, 3.14, {'key': 'open'}, b'byte', ('tuple', 'text'), {1, 1, 3}, None, True, ['list']]
for element in list_of_data:
    print(type(element))
