import sys

input = sys.stdin.readline

r, c, m = map(int, input().split())

result = 0
sharks = {}
dx = [0, 0, 0, 1, -1]
dy = [0, -1, 1, 0, 0]

for i in range(m):
    y, x, s, d, z = map(int, input().split())
    y -= 1
    x -= 1
    
    if d <= 2:
        s %= (r * 2 - 2) if r > 1 else 1
    else:
        s %= (c * 2 - 2) if c > 1 else 1
    
    sharks[(y, x)] = (s, d, z)

for fisher in range(c):
    for depth in range(r):
        if (depth, fisher) in sharks:
            result += sharks[(depth, fisher)][2]
            del sharks[(depth, fisher)]
            break
    
    new_sharks = {}
    
    for (y, x), (s, d, z) in sharks.items():
        ny, nx = y, x
        
        if d <= 2:  # 상하 이동
            cycle = (r - 1) * 2
            if d == 1:  # 위로 이동
                ny = (y - s) % cycle
                if ny >= r:
                    ny = cycle - ny
                    d = 2
                elif ny < 0:
                    ny = -ny
                    d = 2
            else:  # 아래로 이동
                ny = (y + s) % cycle
                if ny >= r:
                    ny = cycle - ny
                    d = 1
        else:  # 좌우 이동
            cycle = (c - 1) * 2
            if d == 3:  # 오른쪽 이동
                nx = (x + s) % cycle
                if nx >= c:
                    nx = cycle - nx
                    d = 4
            else:  # 왼쪽 이동
                nx = (x - s) % cycle
                if nx < 0:
                    nx = -nx
                    d = 3
                elif nx >= c:
                    nx = cycle - nx
                    d = 3
        
        if (ny, nx) not in new_sharks or z > new_sharks[(ny, nx)][2]:
            new_sharks[(ny, nx)] = (s, d, z)
    
    sharks = new_sharks

print(result)