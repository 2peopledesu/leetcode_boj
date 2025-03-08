import sys
import heapq

input = sys.stdin.readline

n = int(input())

lectures = list(list(map(int, input().split())) for _ in range(n))

lectures.sort(key=lambda x: (x[1]))

heap = []
heapq.heappush(heap, lectures[0][2])

for i in range(1, n):
    if lectures[i][1] >= heap[0]:
        heapq.heappop(heap)
    heapq.heappush(heap, lectures[i][2])

print(len(heap))