import sys
sys.setrecursionlimit(10**6) 

input = sys.stdin.readline

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def is_valid(y, x):
    return 0 <= y < n and 0 <= x < m

n, m, k = map(int, input().split())

board = [list(input().rstrip()) for _ in range(n)]

target = input().rstrip()

dp = {}

def dfs(y, x, idx):
    if idx == len(target) - 1:
        return 1
    
    if (y, x, idx) in dp:
        return dp[(y, x, idx)]
    
    count = 0
    
    for d in range(4):
        for nk in range(1, k + 1):
            ny, nx = y + dys[d] * nk, x + dxs[d] * nk
            if is_valid(ny, nx) and board[ny][nx] == target[idx + 1]:
                count += dfs(ny, nx, idx + 1)
    
    dp[(y, x, idx)] = count
    return count

result = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == target[0]:
            result += dfs(i, j, 0)

print(result)