import sys

input = sys.stdin.readline

n, m = map(int, input().split())
k = int(input())

construction = set()
for _ in range(k):
    a, b, c, d = map(int, input().split())
    construction.add((a, b, c, d))
    construction.add((c, d, a, b))

dp = [[0] * (n + 1) for _ in range(m + 1)]
dp[0][0] = 1

for i in range(1, m + 1):
    if (0, i-1, 0, i) not in construction:
        dp[i][0] = dp[i-1][0]

for j in range(1, n + 1):
    if (j-1, 0, j, 0) not in construction:
        dp[0][j] = dp[0][j-1]

for i in range(1, m + 1):
    for j in range(1, n + 1):
        # 위에서 오는 경로
        if (j, i-1, j, i) not in construction:
            dp[i][j] += dp[i-1][j]
        
        # 왼쪽에서 오는 경로
        if (j-1, i, j, i) not in construction:
            dp[i][j] += dp[i][j-1]

print(dp[m][n])