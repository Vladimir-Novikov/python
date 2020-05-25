with open('lesson_5_test.txt', encoding='utf-8') as f:
    lines = f.readlines()
    print(f'В файле {len(lines)} строк')
    for num, word in enumerate(lines, 1):
        print(f'В {num} строке {len(word.split())} слов')
