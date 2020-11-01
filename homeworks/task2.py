"""
Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.

"""

name = input('имя\n>>>')
surname = input('фамилия\n>>>')
year = input('год рождения\n>>>')
city = input('город проживания\n>>>')
email = input('email\n>>>')
phone = input('phone\n>>>')


def data_func(name, surname, year, city, email, phone):
    return (name, surname, year, city, email, phone)


print(*data_func(name=name, surname=surname, year=year, city=city, email=email, phone=phone))

