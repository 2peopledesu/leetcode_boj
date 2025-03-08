from itertools import combinations
import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

set_arr = set(arr)

result = 0

for r in range(2, n + 1):
    for comb in combinations(arr, r):
        set_arr.add(sum(comb))
        
for i in range(1, 2000000):
    if i not in set_arr:
        result = i
        break

print(result)