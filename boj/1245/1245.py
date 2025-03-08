import sys
from collections import deque

# 8방향 탐색 (상하좌우, 대각선)
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def is_peak(grid, visited, n, m, x, y):
    current_h = grid[x][y]
    if current_h == 0:
        return False
    
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    is_valid = True
    
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if grid[nx][ny] > current_h:
                    is_valid = False
                elif grid[nx][ny] == current_h and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    
    return is_valid

def count_peaks(n, m, grid):
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] > 0:
                if is_peak(grid, visited, n, m, i, j):
                    count += 1
    return count

# 입력 처리
n, m = map(int, sys.stdin.readline().split())
grid = []
for _ in range(n):
    grid.append(list(map(int, sys.stdin.readline().split())))

print(count_peaks(n, m, grid))