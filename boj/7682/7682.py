import sys

def is_valid(board):
    x_count = sum(row.count('X') for row in board)
    o_count = sum(row.count('O') for row in board)
    
    if not (x_count == o_count or x_count == o_count + 1):
        return False
    
    x_win = check_win(board, 'X')
    o_win = check_win(board, 'O')
    
    if x_win and o_win:
        return False
    
    if x_win:
        return x_count == o_count + 1
    
    if o_win:
        return x_count == o_count
    
    return (x_count + o_count) == 9

def check_win(board, player):

    for row in board:
        if row.count(player) == 3:
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

while True:
    line = sys.stdin.readline().strip()
    if line == 'end':
        break
    
    board = [list(line[:3]), list(line[3:6]), list(line[6:9])]
    
    if is_valid(board):
        print("valid")
    else:
        print("invalid")