import sys

input = sys.stdin.readline

n = int(input())

# 1. 왼쪽 카드만 통에 버릴 수 있음
# 2. 왼쪽, 오른쪽 둘 다 통에 버릴 경우 얻는 점수 X
# 3. 왼쪽이든 오른쪽이든 남은 카드 없으면 게임 종료
# 4. 오른쪽 카드가 왼쪽 카드보다 작은 경우 점수를 더하고 오른쪽 카드를 버릴 수 있음

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