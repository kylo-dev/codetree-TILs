from collections import deque

def bfs(x, y, k, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    while queue:
        cx, cy = queue.popleft()
        for d in range(4):
            nx, ny = cx + dx[d], cy + dy[d]
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] > k and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny))

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_k = max(max(row) for row in arr)
n_dict = {}

for k in range(1, max_k + 1):
    visited = [[False] * m for _ in range(n)]
    count = 0
    for x in range(n):
        for y in range(m):
            if arr[x][y] > k and not visited[x][y]:
                bfs(x, y, k, visited)
                count += 1
    n_dict[k] = count

max_k, max_count = max(n_dict.items(), key=lambda item: item[1])
print(max_k, max_count)