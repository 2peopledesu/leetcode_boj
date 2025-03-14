from collections import deque


def solution(maps):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    island = 0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] != "X" and visited[i][j] == False:
                queue = deque([(i, j)])
                island += 1
                visited[i][j] = island
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < len(maps) and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X" and visited[nx][ny] == False:
                            visited[nx][ny] = island
                            queue.append((nx, ny))
                            
    answer = [0] * (island)
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if visited[i][j] != False:
                answer[visited[i][j] - 1] += int(maps[i][j])
    
    answer.sort()
    
    return answer if answer else [-1]