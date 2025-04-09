import sys

input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y

n, q = map(int, input().split())

logs = []

for i in range(n):
    x1, x2, y = map(int, input().split())
    logs.append((x1, x2, i + 1))
    
logs.sort()

parents = [i for i in range(n + 1)]

for i in range(n):
    x1, x2, idx = logs[i]
    for j in range(i + 1, n):
        x1_, x2_, idx_ = logs[j]
        if x1_ > x2:
            break
        if max(x1, x1_) <= min(x2, x2_):
            union(idx, idx_)

for _ in range(q):
    a, b = map(int, input().split())
    if find(a) == find(b):
        print("1")
    else:
        print("0")