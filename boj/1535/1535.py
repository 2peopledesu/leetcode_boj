import sys

input = sys.stdin.readline

n = int(input())

lost_hp = list(map(int, input().split()))
get_joy = list(map(int, input().split()))

dp = [0] * 101

for i in range(n):
    for j in range(100, lost_hp[i], -1):
        dp[j] = max(dp[j], dp[j - lost_hp[i]] + get_joy[i])

print(max(dp))