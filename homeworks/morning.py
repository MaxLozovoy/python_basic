class Morning():


    def __init__(self, name):
        self.name = name
        self.morning_time = list(range(7, 11))

    def wake_up(self):
        print('Который сейчас час?')

        while True:
            time = int(input('Введи один из утренних часов с 7 до 11\n>>>'))
            
            if time in self.morning_time:
                print('Жорян, подъем!')
                # return в прогулку
                exit()
            elif time < 7:
                print('Жорян еще дрыхнет!!! Давай попробуем еще раз.')
            elif time > 10:
                print('Ушастый уже проснулся!')
                # return в прогулку
                exit()

            else:
                print('Ошибочка. Поробуй еще раз.')
            # elif anytime in anytime_befor:
            # print('ООО, жорян еще дрыхнет!')
            # exit()
            # elif anytime in anytime_after:
            # print('Ну ты и соня))) Жора уже давно проснулся!!!')
            # exit()

a = Morning('George')
a.wake_up()




