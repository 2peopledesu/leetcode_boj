import sys

def is_in_range(x, y, n):
    return 0 <= x < n and 0 <= y < n

input = sys.stdin.readline

n = int(input().strip())

commands = input().strip()

graph = [list(input().strip()) for _ in range(n)]

light = [[False] * n for _ in range(n)]

zombies = []

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

dxs8, dys8 = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

start_x, start_y, dir = 0, 0, 1 

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'Z':
            zombies.append([i, j, 1])
            graph[i][j] = 'O'

for command in commands:
    if command == 'F':
        nx, ny = start_x + dxs[dir], start_y + dys[dir]
        if is_in_range(nx, ny, n):
            start_x, start_y = nx, ny
            
            if graph[nx][ny] == 'S':
                light[nx][ny] = True
                for turn in range(8):
                    turn_nx, turn_ny = nx + dxs8[turn], ny + dys8[turn]
                    if is_in_range(turn_nx, turn_ny, n):
                        light[turn_nx][turn_ny] = True
    elif command == 'L':
        dir = (dir - 1) % 4
    elif command == 'R':
        dir = (dir + 1) % 4
    
    new_zombies = []
    for zombie in zombies:
        zx, zy, zdir = zombie
        if zx == start_x and zy == start_y and not light[zx][zy] and graph[zx][zy] != 'S':
            print("Aaaaaah!")
            sys.exit()
            
        nzx, nzy = zx + dxs[zdir], zy + dys[zdir]
        
        if is_in_range(nzx, nzy, n):
            zx, zy = nzx, nzy
        else:
            zdir = (zdir + 2) % 4
        
        if zx == start_x and zy == start_y and not light[zx][zy] and graph[zx][zy] != 'S':
            print("Aaaaaah!")
            sys.exit()
            
        new_zombies.append([zx, zy, zdir])
    
    zombies = new_zombies

print("Phew...")