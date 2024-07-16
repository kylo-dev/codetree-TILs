n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dx, dy = (1, 0), (0, 1)

def dfs(x, y):

    if visited[x][y] == 0:
        visited[x][y] = 1
        for i in range(2):
            nx = x + dx[i]
            ny = y + dy[i]
            if -1 < nx < n and -1 < ny < m and arr[nx][ny] == 1:
                dfs(nx, ny)

dfs(0, 0)

print(visited[-1][-1])