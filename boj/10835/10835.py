import sys

input = sys.stdin.readline

n = int(input())

card1 = list(map(int, input().split()))
card2 = list(map(int, input().split()))

dp = [[-1] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(n):
    for j in range(n):
        if dp[i][j] == -1:
            continue
        left = card1[i]
        right = card2[j]
        
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j])
        if right < left:
            dp[i][j + 1] = max(dp[i][j] + right, dp[i][j + 1])

result = 0

for i in range(n + 1):
    result = max(result, dp[n][i], dp[i][n])
    
print(result)