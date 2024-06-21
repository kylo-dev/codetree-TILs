n = int(input())

square = [[0] * 201 for _ in range(201)]

a_list = []
for _ in range(n):
    a_list.append(list(map(int, input().split())))

min_num = min(min(a for a in a_list))
shift = -min(0, min_num)

for a in a_list:
    for x in range(a[0], a[0]+shift+8):
        for y in range(a[1], a[1]+shift+8):
            square[x][y] = 1

print(sum(sum(row) for row in square))