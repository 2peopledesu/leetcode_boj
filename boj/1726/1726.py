import sys
from collections import deque

input = sys.stdin.readline

dxs, dys = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]

left_turn = {1: 4, 2: 3, 3: 1, 4: 2}
right_turn = {1: 3, 2: 4, 3: 2, 4: 1}

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
start_x, start_y, start_dir = map(int, input().split())
end_x, end_y, end_dir = map(int, input().split())

visited = [[[0] * 5 for _ in range(n)] for _ in range(m)]
queue = deque([(start_x - 1, start_y - 1, start_dir, 0)])
visited[start_x - 1][start_y - 1][start_dir] = 1

while queue:
    x, y, d, c = queue.popleft()

    if x == end_x - 1 and y == end_y - 1 and d == end_dir:
        print(c)
        break

    for i in range(1, 4):
        nx, ny = x + dxs[d] * i, y + dys[d] * i

        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            break
        if board[nx][ny] == 1:
            break
        if visited[nx][ny][d] == 0:
            visited[nx][ny][d] = 1
            queue.append((nx, ny, d, c + 1))

    nd = left_turn[d]
    if visited[x][y][nd] == 0:
        visited[x][y][nd] = 1
        queue.append((x, y, nd, c + 1))

    nd = right_turn[d]
    if visited[x][y][nd] == 0:
        visited[x][y][nd] = 1
        queue.append((x, y, nd, c + 1))