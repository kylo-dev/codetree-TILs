import sys
sys.setrecursion(10**6)
n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

n_dict = {}

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_k = [max(row) for row in arr]
k = max(max_k)

def dfs(x, y, k, visited):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] > k and not visited[nx][ny]:
            dfs(nx, ny, k, visited)

for i in range(1, k+1):
    visited = [[False] * m for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] > i and not visited[x][y]:
                dfs(x, y, i, visited)
                count += 1
    n_dict[i] = count

max_k, max_count = max(n_dict.items(), key = lambda x: x[1])
print(max_k, max_count)