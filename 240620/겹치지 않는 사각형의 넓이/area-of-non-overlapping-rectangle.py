a_list = []

square = [[0 for _ in range(2001)] for _ in range(2001)]

for _ in range(3):
    a_list.append(list(map(int, input().split())))

min_num = min(min(a) for a in a_list)

if (min_num < 0):
    tol  = abs(min_num)
    for a in a_list:
        a[0] += tol
        a[1] += tol
        a[2] += tol
        a[3] += tol

for i in range(2):
    for x in range(a_list[i][0], a_list[i][2]):
        for y in range(a_list[i][1], a_list[i][3]):
            square[x][y] = 1

for x in range(a_list[2][0], a_list[2][2]):
    for y in range(a_list[2][1], a_list[2][3]):
        square[x][y] = 0

print(sum(sum(s) for s in square))