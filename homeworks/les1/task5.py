revenue = int(input('Введите величину выручки\n>>>'))
costs = int(input('Введите величину издержек\n>>>'))

finres = revenue - costs

print('Финансовый результат предприятия: ' + str(finres))

if finres > 0:
    profitab = finres / revenue
    print('Рентабельность предприятия: ' + str(round(profitab, 2)))

    staf = int(input('Введите колличество сотрудников\n>>>'))
    profit_per_staf = finres / staf
    print('Прибыль предприятия на одного сотрудника составляет: ' + str(round(profit_per_staf)))
else:
    print('Ваше предприятие убыточно!!!')