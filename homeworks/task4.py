"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.

"""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}


new_file = []
with open('file_task4.txt', 'r', encoding='UTF-8') as my_file:

    for itm in my_file:
        itm = itm.split(' ', 1)
        print(itm)
        new_file.append(rus[itm[0]] + ' ' + itm[1])


with open('new_file_task4.txt', 'w', encoding='UTF-8') as new_my_file:
    new_my_file.writelines(new_file)

with open('new_file_task4.txt', 'r', encoding='UTF-8') as finish_file:
    content = finish_file.read()
    print(content)
