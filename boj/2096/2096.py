import sys

input = sys.stdin.readline

n = int(input())

prev_max = list(map(int, input().split()))
prev_min = prev_max.copy()

for _ in range(n-1):
    a, b, c = map(int, input().split())
    
    curr_max = [
        max(prev_max[0], prev_max[1]) + a,
        max(prev_max[0], prev_max[1], prev_max[2]) + b,
        max(prev_max[1], prev_max[2]) + c
    ]
    
    curr_min = [
        min(prev_min[0], prev_min[1]) + a,
        min(prev_min[0], prev_min[1], prev_min[2]) + b,
        min(prev_min[1], prev_min[2]) + c
    ]
    
    prev_max, prev_min = curr_max, curr_min

print(max(prev_max), min(prev_min))