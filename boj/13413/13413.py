import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    start = input().strip()
    end = input().strip()

    w = b = 0
    for i in range(n):
        if start[i] != end[i]:
            if start[i] == 'W':
                w += 1
            else:
                b += 1

    print(max(w, b))