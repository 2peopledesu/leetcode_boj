import sys
import heapq

class pq:
    def __init__(self):
        self.q = []
        
    def push(self, x):
        heapq.heappush(self.q, x)
        
    def pop(self):
        return heapq.heappop(self.q)
        
    def top(self):
        return self.q[0]
    
    def size(self):
        return len(self.q)

    def empty(self):
        return len(self.q) == 0

input = sys.stdin.readline

n = int(input())

pq = pq()

result = 0

for _ in range(n):
    pq.push(int(input()))
    
while pq.size() > 1:
    pq1 = pq.pop()
    if pq.empty() == False:
        pq2 = pq.pop()
        result += pq1 + pq2
        pq.push(pq1 + pq2)
    else:
        break
    
print(result)