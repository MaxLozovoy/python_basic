"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.

"""

my_file = open('file.txt', 'w', encoding='UTF-')

while True:
    line = input('Введите строку \n>>>')
    if line == ' ':
        break
    my_file.write(line + '\n')

my_file.close()

my_file = open('file.txt', 'r', encoding='UTF-')
content = my_file.read()
print(content)

my_file.close()





