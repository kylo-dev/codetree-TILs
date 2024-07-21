from collections import deque

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

rc = [list(map(int, input().split())) for _ in range(k)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x, y):
    que = deque([])
    que.append((x, y))
    arr[x][y] = 1
    cnt = 1

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 0:
                arr[nx][ny] = 1
                cnt += 1
                que.append((nx, ny))
    return cnt

total = 0

if n == 1:
    if arr[0] == 1:
        print(0)
    else: 
        print(1)
else:
    for i in range(k):
        r, c = rc[i][0], rc[i][1]
        if arr[r-1][c-1] == 0:
            total += bfs(r-1, c-1)
    print(total)