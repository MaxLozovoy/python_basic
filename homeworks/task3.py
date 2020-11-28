"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы:
оклад и премия, например, {"wage": wage, "bonus": bonus}.
Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name)
и дохода с учетом премии (get_total_income).
Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
# словари на который ссылается _income в объекте класса
my_dict = {"wage": 2000, "bonus": 500}
my_dict_1 = {"wage": 5000, "bonus": 300}
class Worker:

    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income




class Position(Worker):
    # метод возвращает имя и фамилию
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    # метод возвращает доход
    def get_total_income(self):
        return f'Доход тотал: {self._income}'



Obj = Position('Иван', 'Иванов', 'manager', sum(my_dict.values()))

print(Obj.get_full_name())
print(Obj.get_total_income())

Obj_1 = Position('Петр', 'Петров', 'manager', sum(my_dict_1.values()))

print(Obj_1.get_full_name())
print(Obj_1.get_total_income())