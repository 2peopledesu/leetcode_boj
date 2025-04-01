import sys
from collections import deque

input = sys.stdin.readline

n = int(input()) 
m = int(input()) 

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
is_basic = [True] * (n + 1)

for _ in range(m):
    x, y, k = map(int, input().split())
    graph[x].append((y, k))
    indegree[y] += 1
    is_basic[x] = False

dp = [0] * (n + 1)
dp[n] = 1

order = []
q = deque()

q.append(n)

while q:
    now = q.popleft()
    order.append(now)
    
    for next_part, _ in graph[now]:
        indegree[next_part] -= 1
        if indegree[next_part] == 0:
            q.append(next_part)

for part in order:
    for next_part, cnt in graph[part]:
        dp[next_part] += dp[part] * cnt

for i in range(1, n):
    if is_basic[i]:
        print(i, dp[i])

print(graph, indegree, is_basic, dp)