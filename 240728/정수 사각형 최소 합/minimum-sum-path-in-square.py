n = int(input())

arr = [
    list(map(int, input().split()))
    for _ in range(n)
]

dp = [
    [0 for _ in range(n)]
    for _ in range(n)
]

def initital():
    dp[0][n-1] = arr[0][n-1]

    for i in range(1, n):
        dp[0][n-1-i] = dp[0][n-1-i+1] + arr[0][n-1-i]
    
    for j in range(1, n):
        dp[j][n-1] = dp[j-1][n-1] + arr[j-1][n-1]

initital()

for i in range(1, n):
    for j in range(n-2, -1, -1):
        dp[i][j] = min(dp[i-1][j] + arr[i][j], dp[i][j+1] + arr[i][j])

print(dp[-1][0])