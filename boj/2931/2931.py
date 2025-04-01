import sys
input = sys.stdin.readline

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

pipe_connections = {
    '|': [False, True, False, True],
    '-': [True, False, True, False],
    '+': [True, True, True, True],
    '1': [True, True, False, False],
    '2': [True, False, False, True],
    '3': [False, False, True, True],
    '4': [False, True, True, False],
    'M': [True, True, True, True],
    'Z': [True, True, True, True]
}

R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().strip()))

M_pos, Z_pos = None, None
for i in range(R):
    for j in range(C):
        if board[i][j] == 'M':
            M_pos = (i, j)
        elif board[i][j] == 'Z':
            Z_pos = (i, j)
            
def check_mz_single_connection():
    m_connections = 0
    z_connections = 0
    
    for d in range(4):
        mx, my = M_pos[0] + dx[d], M_pos[1] + dy[d]
        if 0 <= mx < R and 0 <= my < C and board[mx][my] != '.' and board[mx][my] != 'Z':
            opposite_dir = (d + 2) % 4
            if board[mx][my] in pipe_connections and pipe_connections[board[mx][my]][opposite_dir]:
                m_connections += 1
        
        zx, zy = Z_pos[0] + dx[d], Z_pos[1] + dy[d]
        if 0 <= zx < R and 0 <= zy < C and board[zx][zy] != '.' and board[zx][zy] != 'M':
            opposite_dir = (d + 2) % 4
            if board[zx][zy] in pipe_connections and pipe_connections[board[zx][zy]][opposite_dir]:
                z_connections += 1
    
    return m_connections == 1 and z_connections == 1

def find_missing_pipe():
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                needed_connections = [False, False, False, False]
                
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] != '.':
                        opposite_dir = (d + 2) % 4
                        if board[ni][nj] in pipe_connections and pipe_connections[board[ni][nj]][opposite_dir]:
                            needed_connections[d] = True
                
                if any(needed_connections):
                    simple_pipes = ['|', '-', '1', '2', '3', '4', '+']
                    
                    for pipe_type in simple_pipes:
                        supports_needed = True
                        for d in range(4):
                            if needed_connections[d] and not pipe_connections[pipe_type][d]:
                                supports_needed = False
                                break
                        
                        no_unnecessary = True
                        for d in range(4):
                            if pipe_connections[pipe_type][d] and not needed_connections[d]:
                                no_unnecessary = False
                                break
                        
                        if supports_needed and no_unnecessary:
                            board[i][j] = pipe_type
                            if is_valid_path() and check_mz_single_connection():
                                return i, j, pipe_type
                            board[i][j] = '.'
    
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                needed_connections = [False, False, False, False]
                
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    
                    if 0 <= ni < R and 0 <= nj < C and board[ni][nj] != '.':
                        opposite_dir = (d + 2) % 4
                        if board[ni][nj] in pipe_connections and pipe_connections[board[ni][nj]][opposite_dir]:
                            needed_connections[d] = True
                
                if any(needed_connections):
                    for pipe_type in '|-+1234':
                        board[i][j] = pipe_type
                        if is_valid_path() and check_mz_single_connection():
                            return i, j, pipe_type
                        board[i][j] = '.'
    
    return None

def is_valid_path():
    visited = [[False] * C for _ in range(R)]
    pipe_count = 0
    total_pipes = 0
    z_reached = False
    
    for i in range(R):
        for j in range(C):
            if board[i][j] in '|-+1234MZ':
                total_pipes += 1
    
    def dfs(x, y):
        nonlocal pipe_count, z_reached
        
        if visited[x][y]:
            return
        
        visited[x][y] = True
        pipe_count += 1
        
        if board[x][y] == 'Z':
            z_reached = True
        
        for d in range(4):
            if not pipe_connections[board[x][y]][d]:
                continue
                
            nx, ny = x + dx[d], y + dy[d]
            
            if 0 <= nx < R and 0 <= ny < C and board[nx][ny] != '.':
                opposite_dir = (d + 2) % 4
                if pipe_connections[board[nx][ny]][opposite_dir]:
                    dfs(nx, ny)
    
    dfs(M_pos[0], M_pos[1])
    
    return z_reached and pipe_count == total_pipes

result = find_missing_pipe()

if result:
    i, j, pipe_type = result
    print(i+1, j+1, pipe_type)