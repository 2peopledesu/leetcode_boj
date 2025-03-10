from collections import deque

def solution(maps):

    n, m = len(maps), len(maps[0])
    
    start, lever, exit = None, None, None
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                exit = (i, j)
    
    def bfs(start_pos, end_pos):
        queue = deque([(start_pos, 0)])
        visited = [[False] * m for _ in range(n)]
        visited[start_pos[0]][start_pos[1]] = True
        
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        
        while queue:
            (x, y), time = queue.popleft()
            
            if (x, y) == end_pos:
                return time
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != 'X':
                    visited[nx][ny] = True
                    queue.append(((nx, ny), time + 1))
        
        return -1
    
    to_lever = bfs(start, lever)
    if to_lever == -1:
        return -1 
    
    to_exit = bfs(lever, exit)
    if to_exit == -1:
        return -1 
    
    return to_lever + to_exit