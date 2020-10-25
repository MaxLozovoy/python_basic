dist_a = int(input('Дистанция в первый день\n>>>'))
dist_b = int(input('На какой день спортсен выйдет на дистанцию\n>>>'))
incr_dist = int(input('При ежедневном увеличении дистанции на (%)\n>>>'))

day = 1

while dist_b > dist_a:
        dist_a = (dist_a * (incr_dist/100)) + dist_a
        day += 1
        print(str(day) + '-й день: ' + str(round(dist_a, 2)))

