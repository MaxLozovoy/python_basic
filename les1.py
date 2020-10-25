"""
first_variable_string = "Hello' GB"
first_variable_string2 = 'Hello \'BG'
print(first_variable_string)
print(first_variable_string2)
"""
"""
variable_int = 12 # int целое число
variable_float = 12.122 # float дробное число
"""

#user_name = input('ваше имя\n>>>')
#age = input('ваш возраст\n>>>')
#age = int(age)

#print('hello {0} {1}'.format(user_name, age))
#user_hello_string = f"Привет {user_name} твой возраст {age}"
#print(user_hello_string)

#variable bool = False
#variable bool2 = True

"""
if age > 18:
    print('Доступ к разделу ХХХ')
elif age > 16:
    print('Доступ к боевикам')
elif age > 8:
    print('Доступ к мультикам')
else:
    print('Доступ закрыт')
"""


idx = 0
while idx < 10:
    if idx % 2:
        idx += 3
        continue
    print(idx)
    idx += 1
    #if idx == 6:
     #   print('BREAK')
     #  break

else:
    print('ELSE CYCLE')

