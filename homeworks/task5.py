"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""


with open('file_task5.txt', 'w', encoding='UTF-8') as new_file:
    new_file.writelines(input('Введите числа через пробел:\n>>>'))

with open('file_task5.txt', 'r', encoding='UTF-8') as new_file:
    lines = new_file.readlines()
    # берем строки из файла

    lines = [float(subitm) for itm in lines for subitm in itm.split() if subitm.isdigit()]
    # Раскрываем каждую строку из списка (for itm in whole) и, предварительно превратив ее в список,
    # вытаскиваем из нее по элементу (for subitm in itm.split()). Каждый элемент, если он из цифр (if subitm.isdigit())

    print(sum(lines))

# вторую половину решения подсмотрел у одногрупника











