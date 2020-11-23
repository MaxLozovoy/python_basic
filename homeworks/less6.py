class Auto:

    auto_count = 0
    """
    auto_name = 'Lexus'
    auto_model = 'RX-350'
    auto_year = 2019
    """

    #def on_auto_start(self, auto_name, auto_model, auto_year):
        #print(f'Заводим авто')
        #self.auto_name = auto_name
        #self.auto_model = auto_model
        #self.auto_year = auto_year
        #Auto.auto_count += 1

    def __init__(self):
        Auto.auto_count += 1
        print(Auto.auto_count)



   # def on_auto_stop(self):
        #print(f'Глушим авто')


#a = Auto()
#print(a)
#print(type(a))

#a.on_auto_start('Lexus', 'RX-350', 2019)
#print(a.auto_name)
#print(a.auto_count)

#a.on_auto_stop()

#a_2 = Auto()
#print(a)
#print(type(a))

#a.on_auto_start('Mazda', '6', 2020)
#print(a.auto_name)
#print(a.auto_count)

a_1 = Auto()
a_2 = Auto()
a_3 = Auto()