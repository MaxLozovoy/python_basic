time_sec = input('Введите время в секундах\n>>>')
time_sec_int = int(time_sec)
hours = time_sec_int / 3600

hours_float = float(hours)
hours_int = int(hours)
hours_time = hours_int
hours_balance = hours_float - hours_int

minutes = hours_balance * 60
minutes_int = int(minutes)
minutes_float = float(minutes)
minutes_time = minutes_int
minutes_balance = minutes_float - minutes_int

seconds = minutes_balance * 60
seconds_time = int(seconds)

print('{0}:{1}:{2}'.format(hours_time, minutes_time, seconds_time))
