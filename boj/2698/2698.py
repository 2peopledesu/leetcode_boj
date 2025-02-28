import sys

input = sys.stdin.readline

def solve():
    dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n + 1)]

    dp[1][0][0] = 1
    dp[1][0][1] = 1

    for i in range(2, n + 1):
        for j in range(k + 1):
            dp[i][j][0] = dp[i-1][j][0] + dp[i-1][j][1]
            
            if j > 0:
                dp[i][j][1] += dp[i-1][j-1][1]
            dp[i][j][1] += dp[i-1][j][0]
    
    return dp[n][k][0] + dp[n][k][1]

T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    print(solve())