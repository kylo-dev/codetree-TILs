n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def initial():
    dp[0][0] = arr[0][0]

    ## 아래
    for i in range(1, n):
        dp[i][0] = min(dp[i-1][0], arr[i][0])
    
    # 오른쪽
    for j in range(1, n):
        dp[0][j] = min(dp[0][j-1], arr[0][j])

initial()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), arr[i][j])

print(dp[-1][-1])