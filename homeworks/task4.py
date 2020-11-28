"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.

"""


class Car:

    def __init__(self, speed, color, name, is_police=False):

        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Машина поехала')

    def stop(self):
        print('Машина остановилась')

    def show_speed(self):
        return self.speed

    def turn(self):
        while True:
            # запускаем бесконечный цикл
            comand = input('Укажите направление: s(прямо), r(направо), l(налево), b(назад), f(финиш)\n>>>')

            if comand == 'l':
                print('Машина повернула налево')

            elif comand == 'r':
                print('Машина повернула на лево')

            elif comand == 's':
                print('Машина едет прямо')

            elif comand == 'b':
                print('Машина движется назад')

            elif comand == 'f':
                print('Приехали!!!!')
                break

            else:
                # нужнео выбрать один из преддоженных вариантов, иначе цикл продолжается
                print("Введите одно из предложенных действий.")


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            print('Внимание!!! Превышение скорости!!!')
        else:
            print('Вы молодец!!! не первышаете скороть!!!')



class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)



class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            print('Внимание!!! Превышение скорости')


class PoliceCar(Car, TownCar):
    def __init__(self, speed, color, name):
        self.type = 'police'
        super().__init__(speed, color, name, True)

    #def thives(self):
        #if TownCar.speed(self) > 61:







#town
town = TownCar(62, 'красный', 'Мазда 3')
town.go()
print(town.name)
town.turn()
town.show_speed()
print(f'Ваша скорость {town.speed}')
town.stop()
print('\n \n')
#sport
sport = SportCar(150, 'ченрыный', 'camaro')
print(sport.name)
sport.go()
sport.turn()
print(f'Ваша скорость {sport.speed}')
sport.show_speed()
sport.stop()
print('\n \n')
#police

police = PoliceCar(100, 'белый', 'шевроле')
print(f'Полицейская машина {police.name} {police.color} всегда на посту')
print(police.show_speed())




