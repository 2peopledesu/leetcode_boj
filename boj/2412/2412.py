from collections import deque
import sys

input = sys.stdin.readline
n, t = map(int, input().split())

holds = set()
for _ in range(n):
    x, z = map(int, input().split())
    holds.add((x, z))

queue = deque([(0, 0, 0)])
visited = set([(0, 0)])

def bfs():
    while queue:
        x, z, steps = queue.popleft()
        
        if z == t:
            return steps
        
        for dx in range(-2, 3):
            for dz in range(-2, 3):
                nx, nz = x + dx, z + dz
                
                if (nx, nz) in visited or (nx, nz) not in holds:
                    continue
                
                queue.append((nx, nz, steps + 1))
                visited.add((nx, nz))

    return -1

print(bfs())