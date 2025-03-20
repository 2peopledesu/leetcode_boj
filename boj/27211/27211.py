import sys
from collections import deque

input = sys.stdin.readline

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

n, m = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]

queue = deque()

count = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0 and visited[i][j] == 0:
            count += 1
            visited[i][j] = count
            queue.append((i, j))

            while queue:
                x, y = queue.popleft()
                
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    nx = nx % n
                    ny = ny % m
                    
                    if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                        visited[nx][ny] = count
                        queue.append((nx, ny))

print(max(max(row) for row in visited))