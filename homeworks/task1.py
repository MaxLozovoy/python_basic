"""
Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
"""


number1 = float(input('Введите первое число:\n>>>'))
number2 = float(input('Введите второе число числа:\n>>>'))


def div_numbers(number1, number2):

    try:
        result = number1 / number2
        return result
    except ZeroDivisionError:
        print('На ноль делить нельзя')
        return float('nan')
        # выдает не ошибку а то, что полученный результат неопределенное число


print('Ответ: ', round(div_numbers(number1, number2), 2))

