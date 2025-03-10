import sys
from collections import deque

n = int(sys.stdin.readline())
tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [False] * (n+1)
q = deque()
q.append((1, 0))
total = 0

while q:
    node, depth = q.popleft()
    visited[node] = True
    is_leaf = True

    for neighbor in tree[node]:
        if not visited[neighbor]:
            is_leaf = False
            q.append((neighbor, depth + 1))

    if is_leaf:
        total += depth

print("Yes" if total % 2 == 1 else "No")