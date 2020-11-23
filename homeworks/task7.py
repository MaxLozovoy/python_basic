"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

Подсказка: использовать менеджеры контекста.
"""

import json


with open('file_task7.txt', 'r', encoding='UTF-8') as my_file:
    firms = {}
    total_profit = []



    for line in my_file:
        tmp = line.split(' ')
        name = tmp[0]
        _, form, revenue, costs = line.split()
        profit = int(revenue) - int(costs)
        firms[name] = profit



        if profit >= 0:
            total_profit.append(profit)
            aver_profit = sum(total_profit) // len(total_profit)
            average = {'average profit': aver_profit}

    print(firms)
    print(average)
    print(type(average))

    result = [firms, average]
    print(result)
    print(type(result))


with open('file_task7.json', 'w', encoding='UTF-8') as my_json_file:
    json.dump(result, my_json_file)

with open('file_task7.json', 'r', encoding='UTF-8') as my_json_file_1:
    content = my_json_file_1.read()
    print('JSON_METHOD')
    print(content)
    print(type(content))



