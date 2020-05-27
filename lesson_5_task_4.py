with open('1234.txt', encoding='utf-8') as f:
    numbers = f.readlines()
    new_file = []
    for number in numbers:
        if number.split()[0] == 'One':
            new_file.append(number.replace('One', 'Один'))
        elif number.split()[0] == 'Two':
            new_file.append(number.replace('Two', 'Два'))
        elif number.split()[0] == 'Three':
            new_file.append(number.replace('Three', 'Три'))
        else:
            new_file.append(number.replace('Four', 'Четыре'))

with open('1234_ru.txt', 'w', encoding='utf-8') as f:
    f.writelines(new_file)
