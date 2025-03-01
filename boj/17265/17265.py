import sys

input = sys.stdin.readline

n = int(input())
board = [list(input().split()) for _ in range(n)]
max_result = -float('inf')
min_result = float('inf')

dxs, dys = [0, 1], [1, 0]
visited = [[False for _ in range(n)] for _ in range(n)]

def dfs(x, y, expression, is_operator_next):
    global max_result, min_result
    
    if x == n-1 and y == n-1:
        result = eval(expression)
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    
    for i in range(2):
        nx, ny = x + dxs[i], y + dys[i]
        
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            visited[nx][ny] = True
            
            if is_operator_next:
                dfs(nx, ny, expression + board[nx][ny], False)
            else:
                dfs(nx, ny, "(" + expression + board[nx][ny] + ")", True)
                
            visited[nx][ny] = False

visited[0][0] = True
dfs(0, 0, board[0][0], True)

print(max_result, min_result)