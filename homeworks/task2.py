"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
выполнить подсчет количества строк, количества слов в каждой строке.

"""

with open('file_task2.txt', 'r', encoding='UTF-8') as my_file:

    count_lines = 0


    for line in my_file:
        count_lines += 1

        print(f'В строке: {count_lines}, кол-во слов: {len(line.split())}')
    print(f'Кол-во строк: {count_lines}')



