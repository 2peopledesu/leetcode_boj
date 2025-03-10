import sys
from collections import deque

def is_array(x, y):
    return 0 <= x < m and 0 <= y < n

input = sys.stdin.readline

m, n = map(int, input().split())

arr = [list(map(int, input().strip())) for _ in range(m)]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

visited = [[0] * n for _ in range(m)]

for i in range(n):
    if arr[0][i] == 1:
        continue
    q = deque()
    q.append((0, i))
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            new_x = x + dx
            new_y = y + dy
            if is_array(new_x, new_y):
                if arr[new_x][new_y] == 0 and visited[new_x][new_y] != True:
                    q.append((new_x, new_y))
                    visited[new_x][new_y] = True
    
    for j in range(n):
        if visited[m - 1][j] == True:
            print("YES")
            sys.exit()

print("NO")