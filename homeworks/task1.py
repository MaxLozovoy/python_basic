"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


number1 = int(input('Введите первое число:\n>>>'))
number2 = int(input('Введите второе число числа:\n>>>'))


def div_numbers(number1, number2):

    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        return 'На ноль делить нельзя'


print('Ответ: ', round(div_numbers(number1, number2), 2))

