import sys
from collections import deque

input = sys.stdin.readline

def is_array(x, y):
    return 0 <= x < r and 0 <= y < c

r, c = map(int, input().split())

arr = list(list(input().strip()) for _ in range(r))
dxs, dys = [0, 0, 1, -1], [1, -1, 0, 0]

total_sheep = 0
total_wolf = 0

visited = list([0] * c for _ in range(r))

for i in range(r):
    for j in range(c):
        if not visited[i][j] and arr[i][j] != '#':
            sheep = 0
            wolf = 0
            visited[i][j] = 1
            if arr[i][j] == 'o':
                sheep += 1
            elif arr[i][j] == 'v':
                wolf += 1
            queue = deque([(i, j)])
            flag = True
            while queue:
                x, y = queue.popleft()
                for k in range(4):
                    nx, ny = x + dxs[k], y + dys[k]
                    if not is_array(nx, ny):
                        flag = False
                    if is_array(nx, ny):
                        if not visited[nx][ny] and arr[nx][ny] != '#':
                            visited[nx][ny] = 1
                            if arr[nx][ny] == 'o':
                                sheep += 1
                            elif arr[nx][ny] == 'v':
                                wolf += 1
                            queue.append((nx, ny))
            if not flag:
                sheep = 0
                wolf = 0
                continue
            if sheep > wolf:
                total_sheep += sheep
            else:
                total_wolf += wolf
                
print(total_sheep, total_wolf)