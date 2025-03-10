import sys
input = sys.stdin.readline

n = int(input())
commands = input().strip()

dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
map = [['#' for j in range(101)] for i in range(101)]

x, y, d = 50, 50, 2
max_x = max_y = min_y = min_x = 50
map[x][y] = '.'

for i in commands:
    if(i == 'L'):
        d = (d+3) % 4
    elif(i == 'R'):
        d = (d+1) % 4
    else:
        x = x + dx[d]
        y = y + dy[d]
        map[x][y] = '.'
        min_y, max_y, min_x, max_x = min(min_y, y), max(max_y, y), min(min_x, x), max(max_x, x)
        
for i in range(min_x, max_x+1):
    print(''.join(map[i][min_y:max_y+1]))