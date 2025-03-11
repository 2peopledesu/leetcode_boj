import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
h, w, start_x, start_y, end_x, end_y = map(int, input().split())

start_x -= 1
start_y -= 1
end_x -= 1
end_y -= 1

visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

walls = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            walls.append((i, j))

def can_place(x, y):
    if x < 0 or x + h - 1 >= n or y < 0 or y + w - 1 >= m:
        return False
  
    for wall_x, wall_y in walls:
        if x <= wall_x < x + h and y <= wall_y < y + w:
            return False
    
    return True

def bfs():
    queue = deque([(start_x, start_y, 0)])
    visited[start_x][start_y] = True
    
    while queue:
        x, y, dist = queue.popleft()
        
        if x == end_x and y == end_y:
            return dist
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and can_place(nx, ny):
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
    
    return -1

print(bfs())