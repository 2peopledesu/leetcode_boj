import sys
import heapq

def dijkstra(start, v):
    dist = [float('inf')] * (v + 1)
    dist[start] = 0
    heap = [(0, start)]
    
    while heap:
        current_dist, u = heapq.heappop(heap)
        if dist[u] < current_dist:
            continue
        
        for neighbor, length in graph[u]:
            new_dist = current_dist + length
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    
    return [d if d != float('inf') else -1 for d in dist]

input = sys.stdin.readline

n, v, e = map(int, input().split())

a, b = map(int, input().split())

homes = list(map(int, input().split()))

graph = [[] for _ in range(v + 1)]

for _ in range(e):
    start, dest, length = map(int, input().split())
    graph[start].append((dest, length))
    graph[dest].append((start, length))

dist_a = dijkstra(a, v)
dist_b = dijkstra(b, v)

total = 0
for home in homes:
    total += dist_a[home] + dist_b[home]
    
print(total)
