import sys

input = sys.stdin.readline

t = int(input())

dp = [1] * 10001
for i in range(2, 4):
    for j in range(1, len(dp)):
        if j >= i:
            dp[j] += dp[j - i]

for _ in range(t):
    n = int(input())
    
    print(dp[n])