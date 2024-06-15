m1, d1, m2, d2 = map(int, input().split())

week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

standard = d1
cal_time = d2

for i in range(1, m1):
    standard += day[i]

for j in range(1, m2):
    cal_time += day[j]

if (cal_time > standard):
    cal_day = cal_time - standard
    print(week[cal_day % 7])
else:
    cal_day = abs(cal_time - standard)
    print(week[-cal_day])