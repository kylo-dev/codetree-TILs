n = int(input())

dp = [0] * (1001)

dp[1] = 2
dp[2] = 7
dp[3] = 13

for i in range(4, n+1):
    dp[i] = dp[i-1] + dp[-2]

print(dp[n]%1000000007)