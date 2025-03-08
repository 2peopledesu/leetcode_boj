import sys
from collections import deque

def bfs(start, target):
    visited = [False] * (n+1)
    q = deque()
    q.append((start, 0))
    visited[start] = True
    
    while q:
        current, dist = q.popleft()
        if current == target:
            return dist
        for neighbor in tree[current]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append((neighbor, dist + tree[current][neighbor]))
    return -1

input = sys.stdin.readline

n, m = map(int, sys.stdin.readline().split())
tree = [{} for _ in range(n+1)]  # 1-based indexing

for _ in range(n-1):
    a, b, c = map(int, sys.stdin.readline().split())
    tree[a][b] = c
    tree[b][a] = c

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    visited = [False] * (n+1)
    print(bfs(u, v))