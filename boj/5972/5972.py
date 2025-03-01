import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

dist = [sys.maxsize] * (n + 1)
dist[1] = 0

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # (비용, 노드)
    
    while q:
        cost, now = heapq.heappop(q)
        
        # 현재 비용이 이미 저장된 비용보다 크면 스킵
        if dist[now] < cost:
            continue
            
        # 현재 노드와 연결된 다른 노드들 확인
        for next_node, next_cost in graph[now]:
            total_cost = cost + next_cost
            
            # 더 적은 비용으로 갈 수 있다면 갱신
            if total_cost < dist[next_node]:
                dist[next_node] = total_cost
                heapq.heappush(q, (total_cost, next_node))

dijkstra(1)

print(dist[n])

