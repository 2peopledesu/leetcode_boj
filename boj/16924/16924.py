import sys

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(input().strip()) for _ in range(n)]

cross = []

dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == '*':
            max_k = 0
            k, x, y = 1, i, j
            flag = True
            while True:
                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx * k, y + dy * k
                    if nx < 0 or nx >= n or ny < 0 or ny >= m or board[nx][ny] != '*':
                        flag = False
                        break
                if not flag:
                    break
                if flag:
                    max_k = k
                    k += 1
                    
            if max_k:
                cross.append((i + 1, j + 1, max_k))
                visited[i][j] = True
                for k in range(max_k + 1):
                    for dx, dy in zip(dxs, dys):
                        visited[i + dx * k][j + dy * k] = True

for i in range(n):
    for j in range(m):
        if board[i][j] == '*' and not visited[i][j]:
            print(-1)
            exit()
            
print(len(cross))
for x, y, k in cross:
    print(x, y, k)