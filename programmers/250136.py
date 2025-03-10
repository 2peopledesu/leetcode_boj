from collections import deque

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    oil_size = []
    oil_id = 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(n):
        for j in range(m):
            if land[i][j] == 1 and visited[i][j] == -1:
                q = deque()
                q.append((i, j))
                visited[i][j] = oil_id
                count = 1
                
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < n and 0 <= ny < m and land[nx][ny] == 1 and visited[nx][ny] == -1:
                            visited[nx][ny] = oil_id
                            q.append((nx, ny))
                            count += 1
                
                oil_size.append(count)
                oil_id += 1
    
    col_oil = [0] * m
    for j in range(m):
        oils = set()
        for i in range(n):
            if visited[i][j] != -1:
                oils.add(visited[i][j])
        col_oil[j] = sum(oil_size[id] for id in oils)
    
    return max(col_oil)