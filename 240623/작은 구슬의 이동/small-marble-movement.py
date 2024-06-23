n, t = map(int, input().split())

r, c, d = input().split()
x, y = int(r), int(c)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d_dict = {"R": 0, "L": 2, "U": 3, "D": 1}

direct = d_dict[d]

for i in range(t):
    if (0 < x+dx[direct] <= n) and (0 < y+dy[direct] <= n):
        x += dx[direct]
        y += dy[direct]
    else:
        direct = (direct + 2) % 4

print(x, y)