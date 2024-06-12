m1, d1, m2, d2 = map(int, input().split())

months = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 30, 31, 30]

day1 = 0
day2 = 0

for i in range(1, m1):
    day1 += months[i] 
day1 += d1

for j in range(1, m2):
    day2 += months[j]
day2 += d2

if (day2 - day1 == 0):
    print(1) 
else:
    print(day2 - day1)