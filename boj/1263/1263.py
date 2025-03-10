import sys

input = sys.stdin.readline

n = int(input())

works = [list(map(int, input().split())) for _ in range(n)]

works.sort(key=lambda x: (x[1], x[0]))

start_time = float('inf')
for t, d in reversed(works):
    start_time = min(d, start_time) - t
    if start_time < 0:
        print(-1)
        exit()

print(start_time if start_time >=0 else -1)