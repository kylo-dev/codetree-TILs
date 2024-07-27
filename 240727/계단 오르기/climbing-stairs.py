n = int(input())

dp = [0] * (1001)

dp[2] = 1
dp[3] = 1

def stair(n):
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]

stair(n)

if dp[n] == 0:
    print(0)
else:
    print(dp[2]%10007)