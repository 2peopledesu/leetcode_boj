import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
streetlamp = list(map(int, input().split()))

# 0 ~ n 채워야 함
# 0에서 제일 먼 거리의 가로등, 마지막에서 제일 먼 거리의 가로등, 각 가로등 사이의 제일 먼 거리

result = 0
result = max(result, streetlamp[0], n - streetlamp[m - 1])

for i in range(1, m):
    result = max(result, (streetlamp[i] - streetlamp[i - 1] + 1) // 2)
    
print(result)