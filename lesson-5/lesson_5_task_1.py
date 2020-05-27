with open('text.txt', 'w', encoding='utf-8') as f:
    while True:
        user_text = input('Введите данные (для завершения ввода - пустая строка): ')
        if user_text == '':
            break
        f.writelines((user_text, '\n'))

with open('text.txt', encoding='utf-8') as f:
    print(f.read())
