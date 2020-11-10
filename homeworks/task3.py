"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
Выполнить подсчет средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32

"""
from statistics import mean
total_salary = 0
count = 0
with open('file_task3.txt', 'r', encoding='UTF-8') as my_file:
    print('Сотрудники с зарплатой ниже 20000,00:')
    for line in my_file:
        key, value = line.split()
        salary_list = line.split(' ')
        salary = float(salary_list[1])
        total_salary += salary
        count += 1

        if float(value) < 20000:

            print(key)

    print(f'Средняя зарплата сотрудников: {round((total_salary / count), 2)}')



