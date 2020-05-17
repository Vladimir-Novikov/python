# первая часть программы
def int_func(text):
    return text.title()


user_text = input('Введите текст: ')
print(int_func(user_text))

# вторая часть программы (отличия в том, что во второй части между словами на выходе остается один пробел)
user_words = input('Введите текст: ').split()
for word in user_words:
    print(int_func(word), end=' ')
