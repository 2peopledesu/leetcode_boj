import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    
distance = [-1] * (n + 1)

distance[x] = 0

queue = deque()
queue.append(x)

while queue:
    current = queue.popleft()
    
    for neighbor in graph[current]:
        if distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

result = []
for i in range(1, n + 1):
    if distance[i] == k:
        result.append(i)
        
if not result:
    print(-1)
else:
    for r in sorted(result):
        print(r)