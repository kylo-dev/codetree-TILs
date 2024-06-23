n = int(input())

d_list = [list(map(int, input().split())) for _ in range(n)]

dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

cnt = 0
check = 0

for i in range(n):
    for j in range(n):
        for dx, dy in zip(dxs, dys):
            if (0 <= i+dx < n) and (0 <= j+dy < n) and d_list[i+dx][j+dy] == 1:
                check += 1
        if (check >= 3):
            cnt += 1
        check = 0

print(cnt)