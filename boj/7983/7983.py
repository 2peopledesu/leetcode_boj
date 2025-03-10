import sys

n = int(sys.stdin.readline())
tasks = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
tasks.sort(key=lambda x: -x[1])

current_time = float('inf')

for d, t in tasks:
    current_time = min(t, current_time) - d
    if current_time < 0:
        print(0)
        exit()

print(current_time)