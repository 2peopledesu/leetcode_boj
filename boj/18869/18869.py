import sys
from collections import defaultdict

input = sys.stdin.readline

M, N = map(int, input().split())
space_list = [list(map(int, input().split())) for _ in range(M)]

for i in range(M):
    temp_space = [[idx, num] for idx, num in enumerate(space_list[i])]
    temp_space.sort(key=lambda x: x[1])
    
    compression = 0
    prev = temp_space[0][1]
    temp_space[0][1] = compression
    for j in range(1, N):
        if temp_space[j][1] != prev:
            compression += 1
            prev = temp_space[j][1]
        temp_space[j][1] = compression
    
    temp_space.sort(key=lambda x: x[0])

    for j in range(N):
        space_list[i][j] = temp_space[j][1]

frequency = defaultdict(int)
for row in space_list:
    frequency[tuple(row)] += 1

print(frequency)

result = 0
for cnt in frequency.values():
    result += cnt * (cnt - 1) // 2

print(result)