def solution(board):
    o_count = sum(row.count('O') for row in board)
    x_count = sum(row.count('X') for row in board)
    
    if not (o_count == x_count or o_count == x_count + 1):
        return 0
    
    def check_win(player):
        for i in range(3):
            if board[i] == player * 3:
                return True
        
        for j in range(3):
            if board[0][j] == player and board[1][j] == player and board[2][j] == player:
                return True
        
        if board[0][0] == player and board[1][1] == player and board[2][2] == player:
            return True
        if board[0][2] == player and board[1][1] == player and board[2][0] == player:
            return True
        
        return False
    
    o_win = check_win('O')
    x_win = check_win('X')
    
    if o_win and x_win:
        return 0
    
    if o_win and o_count != x_count + 1:
        return 0
    
    if x_win and o_count != x_count:
        return 0
    
    return 1