import sys

input = sys.stdin.readline

n, k = map(int, input().split())

dp = [sys.maxsize] * (k + 1)

dp[n] = 0

for i in range(n + 1, k + 1):
    if i % 2 == 0:
        dp[i] = min(dp[i - 1] + 1, dp[i//2] + 1, dp[i])
    else:
         dp[i] = min(dp[i - 1] + 1, dp[i])
  
print(dp[k])