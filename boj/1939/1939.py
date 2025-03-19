import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

bridge = defaultdict(dict)

for i in range(m):
    a, b, c = map(int, input().split())
    if b in bridge[a]:
        bridge[a][b] = max(bridge[a][b], c)
    else:
        bridge[a][b] = c
        
    if a in bridge[b]:
        bridge[b][a] = max(bridge[b][a], c)
    else:
        bridge[b][a] = c
    
start, end = map(int, input().split())

max_min = [-1] * (n + 1)
heap = []
heapq.heappush(heap, (-float('inf'), start))
max_min[start] = float('inf')

while(heap):
    current_min, current_node = heapq.heappop(heap)
    current_min = -current_min
    
    if current_node == end:
        print(current_min)
        break
    
    if current_min < max_min[current_node]:
        continue
    
    for neighbor in bridge[current_node]:
        weight = bridge[current_node][neighbor]
        new_min = min(current_min, weight)
        
        if new_min > max_min[neighbor]:
            max_min[neighbor] = new_min
            heapq.heappush(heap, (-new_min, neighbor))