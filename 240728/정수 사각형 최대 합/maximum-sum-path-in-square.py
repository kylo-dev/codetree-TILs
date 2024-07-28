n = int(input())

num = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def initialize():
    dp[0][0] = num[0][0]

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + num[i][0]
    
    for i in range(1, n):
        dp[0][i] = dp[0][i-1] + num[0][i]

initialize()

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j] + num[i][j], dp[i][j-1] + num[i][j])

print(dp[-1][-1])