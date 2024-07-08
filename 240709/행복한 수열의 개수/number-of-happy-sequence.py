n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

cnt = 0

for i in range(n):
    n_cnt = 1
    for j in range(n-1):
        if arr[i][j] == arr[i][j+1]:
            n_cnt += 1
    if n_cnt >= m:
        cnt += 1
    
for i in range(n):
    n_cnt = 1
    for j in range(n-1):
        if arr[j][i] == arr[j+1][i]:
            n_cnt += 1
    if n_cnt >= m:
        cnt += 1

print(cnt)