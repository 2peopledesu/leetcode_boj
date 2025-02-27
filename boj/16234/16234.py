import sys

input = sys.stdin.readline

def is_array(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

N, L, R = map(int, input().split())

Nation = list(list(map(int, input().split())) for _ in range(N))

open_border = []

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

count = 0

while(True):
    visited = list([False] * N for _ in range(N))
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            stack = [(i, j)]
            union = [(i, j)]
            visited[i][j] = True
            
            while(stack):
                now_x, now_y = stack.pop()
                for k in range(4):
                    next_x, next_y = now_x + dx[k], now_y + dy[k]
                    if not is_array(next_x, next_y) or visited[next_x][next_y]:
                        continue
                    
                    popular_gap = abs(Nation[now_x][now_y] - Nation[next_x][next_y])
                    if L <= popular_gap <= R:
                        stack.append((next_x, next_y))
                        visited[next_x][next_y] = True
                        union.append((next_x, next_y))
            
            if len(union) >= 2:
                open_border.append(union)
    if open_border == []:
        break
    else:
        count += 1
        for elem in open_border:
            total = 0
            open_nation_len = len(elem)
            
            for open_nation in elem:
                total += Nation[open_nation[0]][open_nation[1]]
            
            new_population = total // len(elem)
            
            for open_nation in elem:
                Nation[open_nation[0]][open_nation[1]] = new_population
    
    open_border = []
    
print(count)