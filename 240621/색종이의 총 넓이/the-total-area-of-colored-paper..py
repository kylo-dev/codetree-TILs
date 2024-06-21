n = int(input())

square = [[0] * 201 for _ in range(201)]

a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))

min_x = min(a[0] for a in a_list)
min_y = min(a[1] for a in a_list)
shift_x = -min(0, min_x)
shift_y = -min(0, min_y)

for a in a_list:
    for x in range(a[0]+shift_x, a[0]+shift_x+8):
        for y in range(a[1]+shift_y, a[1]+shift_y+8):
            square[x][y] = 1

print(sum(sum(row) for row in square))