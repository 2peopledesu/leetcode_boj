from collections import deque

def solution(board):
    rows, cols = len(board), len(board[0])
    
    robot_pos, goal_pos = None, None
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == 'R':
                robot_pos = (i, j)
            elif board[i][j] == 'G':
                goal_pos = (i, j)
    
    visited = [[False] * cols for _ in range(rows)]
    visited[robot_pos[0]][robot_pos[1]] = True
    
    queue = deque([(robot_pos, 0)])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    while queue:
        (r, c), moves = queue.popleft()
        
        if (r, c) == goal_pos:
            return moves
        
        for dr, dc in directions:
            nr, nc = r, c
            
            while 0 <= nr + dr < rows and 0 <= nc + dc < cols and board[nr + dr][nc + dc] != 'D':
                nr += dr
                nc += dc
            
            if not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append(((nr, nc), moves + 1))
    
    return -1