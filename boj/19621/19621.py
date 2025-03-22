import sys
input = sys.stdin.readline

n = int(input())
conference = []
for _ in range(n):
    s, e, p = map(int, input().split())
    conference.append((e, s, p))

conference.sort()

dp = [0] * (n+1)
dp[1] = conference[0][2]

for i in range(2, n+1):
    current_s = conference[i-1][1]
    dp[i] = max(dp[i-1], conference[i-1][2])
    
    for j in range(i-2, -1, -1):
        if conference[j][0] < current_s:
            dp[i] = max(dp[i], dp[j+1] + conference[i-1][2])
            break

print(dp[n])