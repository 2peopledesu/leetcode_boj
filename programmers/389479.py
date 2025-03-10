import heapq

def solution(players, m, k):
    answer = 0
    heap = [] 
    
    for time in range(24):
        while heap and heap[0] <= time:
            heapq.heappop(heap)
        
        active_servers = len(heap)
        
        required = players[time] - (active_servers * m)
        if required >= m:
            answer += required // m
            for _ in range(required // m):
                heapq.heappush(heap, time + k)
    
    return answer