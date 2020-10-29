"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через через dict.

"""

month = int(input('Для того что бы узнать время года, введите номер месяца\n>>>'))
my_dict = {1: 'Зима', 2: 'Весна', 3: 'Осень'}
if month == 12 or month == 1 or month == 2:
    print(my_dict.values(1))
elif month == 3 or month == 4 or month == 5:
    print(my_dict.values(2))
elif month == 6 or month == 7 or month == 8:
    print(my_dict.values(3))
elif month == 9 or month == 10 or month == 11:
    print(my_dict.values(4))