n, m = map(int, input().split())

arr = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
vertex_cnt = 0


def dfs(vertex):
    global vertex_cnt

    for cur in arr[vertex]:
        if not visited[cur]:
            visited[cur] = True
            vertex_cnt += 1
            dfs(cur)

for i in range(m):
    v1, v2 = map(int, input().split())

    arr[v1].append(v2)
    arr[v2].append(v1)

visited[1] = True
dfs(1)

print(vertex_cnt)