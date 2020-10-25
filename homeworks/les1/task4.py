number = int(input('Введите целое положительное число\n>>>'))
number_max = number % 10
number = number // 10

while number > 0:
    if number % 10 > number_max:
        number_max = number % 10
    number = number // 10

print('Максимальное число: ' + str(number_max))