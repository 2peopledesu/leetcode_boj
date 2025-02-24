import sys

input = sys.stdin.readline

D, K = map(int, input().split())

dp = [0 for _ in range(D)]

dp[0], dp[1] = 1, 1

while(1):
    for i in range(2, D):
        dp[i] = dp[i - 2] + dp[i - 1]
    
    if dp[D - 1] == K:
        print(dp[0])
        print(dp[1])
        break
    
    if dp[D - 1] > K:
        dp[0] += 1
        dp[1] = dp[0]
    else:
        dp[1] += 1