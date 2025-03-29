import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

start, end = map(int, input().split())

dist = [float('inf')] * (n+1)
dist[start] = 0

q = []
heapq.heappush(q, (0, start))

while q:
    cost, now = heapq.heappop(q)
    if dist[now] < cost:
        continue
    for i, j in graph[now]:
        if dist[i] > cost + j:
            dist[i] = cost + j
            heapq.heappush(q, (dist[i], i))

print(dist[end])