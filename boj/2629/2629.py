import sys

input = sys.stdin.readline

n = int(input())

weight = list(map(int, input().split()))

ball = int(input())

ball_weight = list(map(int, input().split()))

dp = [False] * (sum(weight) + 1)
dp[0] = True

for i in range(n):
    temp = []
    for j in range(len(dp)):
        if dp[j]:
            if j + weight[i] <= sum(weight):
                temp.append(j + weight[i])
            temp.append(abs(j - weight[i]))
    
    for value in temp:
        dp[value] = True

result = []
for i in ball_weight:
    if i > sum(weight) or not dp[i]:
        result.append("N")
    else:
        result.append("Y")

print(" ".join(result))
