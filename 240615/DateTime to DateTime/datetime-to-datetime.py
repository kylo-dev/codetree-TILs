a, b, c = map(int, input().split())

standard = 11 * 24 * 60 + (11 * 60 + 11)

cal_time = a * 24 * 60 + (b * 60 + c)

print(cal_time - standard)