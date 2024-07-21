n = int(input())

n_list = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

def dfs(x, y):

    visited[x][y] = 1
    count = 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] == 1 and not visited[nx][ny]:
            count += dfs(nx, ny)
    
    return count

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and not visited[i][j]:
            n_list.append(dfs(i,j))

print(len(n_list))
for i in sorted(n_list):
    print(i)