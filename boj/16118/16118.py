from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = defaultdict(list)

for i in range(m):
    a, b, d = map(int, input().split())
    dict[a].append((b, d))
    dict[b].append((a, d))
    
fox_pq = [sys.maxsize for _ in range(n + 1)]
fox_pq[1] = 0
fox_heap = []

# 늑대는 [달리는 상태일 때 최소 시간, 걷는 상태일 때 최소 시간]을 저장
wolf_pq = [[sys.maxsize, sys.maxsize] for _ in range(n + 1)]
wolf_pq[1] = [0, sys.maxsize]  # 시작은 달리는 상태(0번 인덱스)로 초기화
wolf_heap = []

heapq.heappush(fox_heap, (0, 1))
# 늑대 힙: (최소 시간, 현재 위치, 현재 상태)
# 상태 0: 달리는 상태 (2배 속도)
# 상태 1: 걷는 상태 (1/2 속도)
heapq.heappush(wolf_heap, (0, 1, 0))  # 처음에는 달리는 상태(0)로 시작

def fox():
    while fox_heap:
        min_dist, min_index = heapq.heappop(fox_heap)
        
        if min_dist > fox_pq[min_index]:
            continue
        
        for next_index, dist in dict[min_index]:
            new_dist = fox_pq[min_index] + dist
            if new_dist < fox_pq[next_index]:
                fox_pq[next_index] = new_dist
                heapq.heappush(fox_heap, (new_dist, next_index))

def wolf():
    while wolf_heap:
        min_dist, min_index, state = heapq.heappop(wolf_heap)
        
        if min_dist > wolf_pq[min_index][state]:
            continue
        
        # 다음 상태 계산 (0->1, 1->0)
        next_state = 1 - state
        
        # 현재 상태에 따른 속도 설정
        # state=0: 달리는 상태 (2배 속도)
        # state=1: 걷는 상태 (1/2 속도)
        speed = 0.5 if state == 1 else 2.0
        
        for next_index, dist in dict[min_index]:
            # 현재 상태의 속도로 다음 지점까지 이동
            new_dist = wolf_pq[min_index][state] + dist / speed
            if new_dist < wolf_pq[next_index][next_state]:
                wolf_pq[next_index][next_state] = new_dist
                heapq.heappush(wolf_heap, (new_dist, next_index, next_state))

result = 0

fox()
wolf()

for i in range(1, n + 1):
    # 각 그루터기까지 늑대의 최소 시간 계산
    wolf_min_time = min(wolf_pq[i][0], wolf_pq[i][1])
    
    # 여우가 늑대보다 먼저 도착할 수 있으면 결과 증가
    if fox_pq[i] < wolf_min_time:
        result += 1

print(result)