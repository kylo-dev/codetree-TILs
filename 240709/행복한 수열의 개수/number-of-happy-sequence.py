n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

seq = []
num_hap = 0

def is_happy():
    con_cnt, max_cnt = 1, 1
    for i in range(1, n):
        if seq[i] == seq[i-1]:
            con_cnt += 1
        else:
            con_cnt = 1
        max_cnt = max(con_cnt, max_cnt)
    
    return max_cnt >= m

# 가로
for i in range(n):
    seq = arr[i][:]

    if is_happy():
        num_hap += 1

# 세로
for i in range(n):
    for j in range(n):
        seq[j] = arr[j][i]
    if is_happy():
        num_hap += 1

print(num_hap)