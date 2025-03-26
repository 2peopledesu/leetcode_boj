import sys

input = sys.stdin.readline
n, m = map(int, input().split())
grid = [list(input().rstrip()) for _ in range(n)]

left = [[0]*m for _ in range(n)]
right = [[0]*m for _ in range(n)]
up = [[0]*m for _ in range(n)]
down = [[0]*m for _ in range(n)]

for i in range(n):
    current = 0
    for j in range(m):
        if grid[i][j] == '#':
            current += 1
        else:
            current = 0
        left[i][j] = current

for i in range(n):
    current = 0
    for j in range(m-1, -1, -1):
        if grid[i][j] == '#':
            current += 1
        else:
            current = 0
        right[i][j] = current

for j in range(m):
    current = 0
    for i in range(n):
        if grid[i][j] == '#':
            current += 1
        else:
            current = 0
        up[i][j] = current
        
for j in range(m):
    current = 0
    for i in range(n-1, -1, -1):
        if grid[i][j] == '#':
            current += 1
        else:
            current = 0
        down[i][j] = current

crosses = []
for i in range(n):
    for j in range(m):
        if grid[i][j] != '#':
            continue
        max_up = up[i][j] - 1
        max_down = down[i][j] - 1
        max_left = left[i][j] - 1
        max_right = right[i][j] - 1
        k_max = min(max_up, max_down, max_left, max_right)
        if k_max < 0:
            continue
        for k in range(k_max + 1):
            crosses.append((i, j, k))

max_product = 0

def check_overlap(i1, j1, k1, i2, j2, k2):
    cross1 = set()
    for di in range(-k1, k1+1):
        cross1.add((i1+di, j1))
    for dj in range(-k1, k1+1):
        cross1.add((i1, j1+dj))
    
    for di in range(-k2, k2+1):
        if (i2+di, j2) in cross1:
            return True
    for dj in range(-k2, k2+1):
        if (i2, j2+dj) in cross1:
            return True
    return False

for a in range(len(crosses)):
    i1, j1, k1 = crosses[a]
    
    for b in range(a + 1, len(crosses)):
        i2, j2, k2 = crosses[b]
        
        if not check_overlap(i1, j1, k1, i2, j2, k2):
            area1 = 4 * k1 + 1
            area2 = 4 * k2 + 1
            max_product = max(max_product, area1 * area2)

print(max_product)