import sys
from collections import deque

input = sys.stdin.readline

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())

before = [list(map(int, input().split())) for _ in range(n)]
after = [list(map(int, input().split())) for _ in range(n)]

different_found = False
different_start_x, different_start_y = 0, 0
start_color, target_color = 0, 0

for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            different_start_x, different_start_y = i, j
            start_color = before[i][j]
            target_color = after[i][j]
            different_found = True
            break
    if different_found:
        break

if not different_found:
    print("YES")
    sys.exit()

queue = deque([(different_start_x, different_start_y)])
visited = [[False] * m for _ in range(n)]
visited[different_start_x][different_start_y] = True

while queue:
    x, y = queue.popleft()
    before[x][y] = target_color
    
    for i in range(4):
        next_x, next_y = x + dxs[i], y + dys[i]
        if 0 <= next_x < n and 0 <= next_y < m and not visited[next_x][next_y]:
            if before[next_x][next_y] == start_color:
                queue.append((next_x, next_y))
                visited[next_x][next_y] = True

for i in range(n):
    for j in range(m):
        if before[i][j] != after[i][j]:
            print("NO")
            sys.exit()

print("YES")