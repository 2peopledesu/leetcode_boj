import sys
from itertools import combinations

def is_valid(x, y):
    return 0 <= x < n and 0 <= y < n and (arr[x][y] == "0" or arr[x][y] == "2")

def bfs(virus, empty_count):
    global answer
    queue = []
    visited = [[False] * n for _ in range(n)]
    
    for x, y in virus:
        queue.append((x, y, 0))
        visited[x][y] = True
        empty_count -= 1
        
    while queue:
        x, y, time = queue.pop(0)
        
        if answer != -1:
            if time >= answer:
                return
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if is_valid(nx, ny) and not visited[nx][ny]:
                queue.append((nx, ny, time + 1))
                
                visited[nx][ny] = True
                
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and (arr[i][j] == "0" or arr[i][j] == "2"):
                return
        
    if answer == -1:
        answer = time
    else:
        answer = min(answer, time)
    
    return

input = sys.stdin.readline

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

n, m = map(int, input().split())

arr = list(list(input().split()) for _ in range(n))

can_input_virus = []

empty_count = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == "2":
            can_input_virus.append((i, j))
            empty_count += 1
        elif arr[i][j] == "0":
            empty_count += 1
        
            
permutations_virus = list(combinations(can_input_virus, m))


answer = -1

for virus in permutations_virus:
    bfs(virus, empty_count)
    
print(answer)