import sys
import heapq

input = sys.stdin.readline

n = int(input())
using_time = []

for _ in range(n):
    a, b = map(int, input().split())
    using_time.append((a, b))

using_time.sort(key=lambda x: x[0])
computers = [0] * n 
end_time = []
available_seats = []

start, end = using_time[0]
computers[0] = 1
heapq.heappush(end_time, (end, 0))
max_computer = 1 

for i in range(1, n):
    start, end = using_time[i]
    
    while end_time and end_time[0][0] <= start:
        _, computer_idx = heapq.heappop(end_time)
        heapq.heappush(available_seats, computer_idx)
    
    if available_seats:
        idx = heapq.heappop(available_seats)
        computers[idx] += 1
        heapq.heappush(end_time, (end, idx))
    else:
        idx = max_computer
        computers[idx] += 1
        max_computer += 1
        heapq.heappush(end_time, (end, idx))

required_computers = 0
result = []
for i in range(n):
    if computers[i] > 0:
        required_computers += 1
        result.append(str(computers[i]))
    else:
        break

print(required_computers)
print(" ".join(result))