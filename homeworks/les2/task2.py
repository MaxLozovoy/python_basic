"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().

"""
user_list = list(input('Введите любые значения кол-вом более одного\n>>>'))

lenth = len(user_list)

if lenth % 2 == 0:
    i = 0
    while i < lenth:
        el = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = el
        i += 2
else:
    i = 0
    while i < lenth - 1:
        el = user_list[i]
        user_list[i] = user_list[i + 1]
        user_list[i + 1] = el
        i += 2

print(user_list)