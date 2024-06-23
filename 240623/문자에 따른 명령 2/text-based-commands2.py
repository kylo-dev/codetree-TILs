d_list = list(input())

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

x, y = 0, 0
direct = 2

for d in d_list:
    if (d == 'L'):
        direct = (direct - 1) % 4
    elif (d == 'R'):
        direct = (direct + 1) % 4
    elif (d == 'F'):
        x += dx[direct]
        y += dy[direct]

print(x, y)