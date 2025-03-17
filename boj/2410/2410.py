import sys

input = sys.stdin.readline

mod = 1000000000

n = int(input())

dp = [0] * (n + 1)
dp[1] = 1
if n > 1:
    dp[2] = 2

for i in range(2, n + 1):
    if i % 2 == 1:
        dp[i] = dp[i - 1] 
    else:
        dp[i] = (dp[i - 1] + dp[i // 2]) % mod
    
print(dp[n])