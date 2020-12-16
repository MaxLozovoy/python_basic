class George_barks():

    def __init__(self, name):
        self.name = name


    def knock_on_the_door(self):
        print('А что будет если кто-то постучит в дверь?')

        while True:
            knock = input('Напиши тук тук тук \n>>>')
            if knock == 'тук тук тук':
                print('Гав! Гав! Гав! Гав!\nЖорян бежит к двери и прыгает на нее как сумасшедший!!!')
                print('Похвали его. Он собака и это его работа!')
                while True:
                    good_boy = input('Напиши молодец\n>>>')
                    if good_boy == 'молодец':
                        print('Жора доволен и машет хвостом!!!')
                        #выход заменить на return когда будет класс MAP
                        exit()
                    else:
                        print('Наверное ты ошибся в слове молодец. Поробуй еще раз!')

            else:
                print('Наверное ты написал не тук тук тук. Поробуй еще раз!')

a = George_barks('George')
a.knock_on_the_door()







