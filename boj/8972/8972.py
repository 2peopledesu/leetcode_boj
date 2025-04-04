import sys

input = sys.stdin.readline

dxs, dys = [1, 1, 1, 0, 0, 0, -1, -1, -1], [-1, 0, 1, -1, 0, 1, -1, 0, 1]

r, c = map(int, input().split())

board = [list(input().rstrip()) for _ in range(r)]
orders = list(map(int, input().rstrip()))
count = 0

enemys = []

for i in range(r):
    for j in range(c):
        if board[i][j] == 'I':
            start = (i, j)
            board[i][j] = '.'
        elif board[i][j] == 'R':
            enemys.append((i, j))
            board[i][j] = '.'
            
def is_valid(x, y):
    return 0 <= x < r and 0 <= y < c
            
for order in orders:
    order -= 1
    start = (start[0] + dxs[order], start[1] + dys[order])
    
    if start in enemys:
        print(f"kraj {count + 1}")
        sys.exit(0)
    
    count += 1
    
    new_positions = []
    for enemy in enemys:
        now_far = abs(start[0] - enemy[0]) + abs(start[1] - enemy[1])
        
        next_x, next_y = enemy[0], enemy[1]
        
        for j in range(9):
            enemy_x = enemy[0] + dxs[j]
            enemy_y = enemy[1] + dys[j]
            
            if not is_valid(enemy_x, enemy_y):
                continue
            
            new_distance = abs(start[0] - enemy_x) + abs(start[1] - enemy_y)
            if now_far > new_distance:
                next_x = enemy_x
                next_y = enemy_y
                now_far = new_distance
        
        new_positions.append((next_x, next_y))
    
    if start in new_positions:
        print(f"kraj {count}")
        sys.exit(0)
    
    position_count = {}
    for pos in new_positions:
        position_count[pos] = position_count.get(pos, 0) + 1
    
    enemys = [pos for pos in position_count if position_count[pos] == 1]

board = [['.' for _ in range(c)] for _ in range(r)]
board[start[0]][start[1]] = 'I'

for enemy in enemys:
    board[enemy[0]][enemy[1]] = 'R'

for row in board:
    print(''.join(row))