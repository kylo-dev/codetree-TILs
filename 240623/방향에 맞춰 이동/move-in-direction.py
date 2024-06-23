n = int(input())

dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

x, y = 0, 0

for i in range(n):
    direct, dist = input().split()
    
    if (direct == 'W'):
        x += dx[0] * int(dist)
    elif (direct == 'S'):
        y += dy[1] * int(dist)
    elif (direct == 'N'):
        y += dy[2] * int(dist)
    elif (direct == 'E'):
        x += dx[3] * int(dist)

print(x, y)