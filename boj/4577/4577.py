import sys

input = sys.stdin.readline

def is_array(x, y, r, c):
    return 0 <= x < r and 0 <= y < c

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

directions = {'U': 0, 'D': 1, 'L': 2, 'R': 3}

game_number = 1

while True:
    r, c = map(int, input().split())
    if r == 0 and c == 0:
        break
        
    board = [list(input().rstrip()) for _ in range(r)]
    
    orders = input().rstrip()
    
    start_x, start_y = 0, 0
    goals = []
    
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'w' or board[i][j] == 'W':
                start_x, start_y = i, j
                if board[i][j] == 'W':
                    goals.append((i, j))
            elif board[i][j] == '+' or board[i][j] == 'B':
                goals.append((i, j))
    
    game_complete = False
    
    for dir in orders:
        if game_complete:
            continue
            
        order = directions[dir]
        next_x, next_y = start_x + dxs[order], start_y + dys[order]
        
        if is_array(next_x, next_y, r, c) and board[next_x][next_y] != '#':

            if board[next_x][next_y] in ['b', 'B']:
                box_next_x, box_next_y = next_x + dxs[order], next_y + dys[order]
                
                if is_array(box_next_x, box_next_y, r, c) and board[box_next_x][box_next_y] not in ['#', 'b', 'B']:
                    
                    is_goal = board[box_next_x][box_next_y] == '+'
                    board[box_next_x][box_next_y] = 'B' if is_goal else 'b'
                    
                    was_on_goal = board[next_x][next_y] == 'B'
                    board[next_x][next_y] = '+' if was_on_goal else '.'
                    
                    is_player_on_goal = board[start_x][start_y] == 'W'
                    board[start_x][start_y] = '+' if is_player_on_goal else '.'
                    
                    start_x, start_y = next_x, next_y
                    is_new_pos_goal = was_on_goal
                    board[start_x][start_y] = 'W' if is_new_pos_goal else 'w'
                else:
                    continue
            else:
                is_player_on_goal = board[start_x][start_y] == 'W'
                board[start_x][start_y] = '+' if is_player_on_goal else '.'
                
                start_x, start_y = next_x, next_y
                is_new_pos_goal = board[next_x][next_y] == '+'
                board[start_x][start_y] = 'W' if is_new_pos_goal else 'w'
        
        all_boxes_on_goals = True
        for i in range(r):
            for j in range(c):
                if board[i][j] == 'b':
                    all_boxes_on_goals = False
                    break
            if not all_boxes_on_goals:
                break
        
        game_complete = all_boxes_on_goals
    
    print(f"Game {game_number}: {'complete' if game_complete else 'incomplete'}")
    for row in board:
        print(''.join(row))
    
    game_number += 1