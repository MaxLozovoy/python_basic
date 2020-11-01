"""
Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
"""

arg1 = int(input('Введите первый аргумент\n>>>'))
arg2 = int(input('Введите второй аргумент\n>>>'))
arg3 = int(input('Введите третий аргумент\n>>>'))


def my_calc(arg1, arg2, arg3):
    my_object = (arg1, arg2, arg3)
    return arg1 + arg2 + arg3 - min(my_object)


print(my_calc(arg1, arg2, arg3))