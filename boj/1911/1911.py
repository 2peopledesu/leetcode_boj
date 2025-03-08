import sys

input = sys.stdin.readline

n, l = map(int, input().split())

puddles = list(list(map(int, input().split())) for _ in range(n))
puddles.sort()

count = 0
current_end = 0

for start, end in puddles:
    if current_end > start:
        start = current_end
    if start >= end:
        continue
    need_count = (end - start + l - 1) // l
    count += need_count
    current_end = start + need_count * l

print(count)