a_list = [list(map(int, input().split())) for _ in range(3)]

min_x = min(a[0] for a in a_list)
min_y = min(a[1] for a in a_list)
max_x = min(a[2] for a in a_list)
max_y = min(a[3] for a in a_list)

shift_x = -min(0, min_x)
shift_y = -min(0, min_y)

square = [[0] * (2001) for _ in range(2001)]

for i in range(2):
    for x in range(a_list[i][0] + shift_x, a_list[i][2] + shift_x):
        for y in range(a_list[i][1] + shift_y, a_list[i][3] + shift_y):
            square[x][y] = 1

for x in range(a_list[2][0] + shift_x, a_list[2][2] + shift_x):
    for y in range(a_list[2][1] + shift_y, a_list[2][3] + shift_y):
        square[x][y] = 0

print(sum(sum(s) for s in square))