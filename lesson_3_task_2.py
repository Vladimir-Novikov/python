def user_data(name, surname, year, city, email, phone):
    print(f'Имя: {name}, фамилия: {surname}, год рождения: {year}, город: {city}, почта: {email}, телефон: {phone}')


user = {'имя': '', 'фамилию': '', 'год рождения': '', 'город': '', 'email': '', 'телефон': ''}
for data in user.keys():
    user[data] = input(f'Введите {data}: ')

user_data(name=user['имя'], surname=user['фамилию'], year=user['год рождения'], city=user['город'], email=user['email'],
          phone=user['телефон'])
