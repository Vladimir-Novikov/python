with open('salary.txt', encoding='utf-8') as f:
    text = f.readlines()
    total = 0
    for el in text:
        average = float((el.split()[1]))
        total = total + average
        if float(el.split()[1]) < 20000:
            print(el.split()[0], el.split()[1])
    print(f'Средняя величина дохода сотрудников: {total / len(text):.2f}')
