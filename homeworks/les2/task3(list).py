"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list.

"""

month = int(input('Для того что бы узнать время года, введите номер месяца\n>>>'))
season_list = list(('Зима', 'Весна', 'Лето', 'Осень'))

if month == 12 or month == 1 or month == 2:
    print(season_list[0])
elif month == 3 or month == 4 or month == 5:
    print(season_list[1])
elif month == 6 or month == 7 or month == 8:
    print(season_list[2])
elif month == 9 or month == 10 or month == 11:
    print(season_list[3])