import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
pq = []

for _ in range(m):
    a, b = map(int, input().split())
    # a를 b보다 먼저 풀어야 함 (a -> b)
    graph[a].append(b)
    indegree[b] += 1

# 진입 차수가 0인 정점을 우선순위 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

result = []
while pq:
    # 가장 작은 번호(쉬운 문제)를 꺼냄
    now = heapq.heappop(pq)
    result.append(now)
    
    # 현재 노드와 연결된 다음 노드들의 진입 차수 감소
    for next_node in graph[now]:
        indegree[next_node] -= 1
        # 진입 차수가 0이 되면 큐에 삽입
        if indegree[next_node] == 0:
            heapq.heappush(pq, next_node)

print(*result)