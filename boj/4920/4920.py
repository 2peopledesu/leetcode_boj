import sys

input = sys.stdin.readline

tetrominos = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (0, 1), (0, 2), (1, 0)],
    [(0, 0), (0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 0), (1, 1), (1, 2)],
    
    [(0, 1), (1, 1), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (2, 0)],
    [(0, 0), (0, 1), (0, 2), (1, 2)],
    
    [(0, 0), (0, 1), (0, 2), (1, 1)],
    [(0, 1), (1, 0), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (1, 1), (1, 2)],
    [(0, 0), (1, 0), (1, 1), (2, 0)],
    
    [(0, 1), (0, 2), (1, 0), (1, 1)],
    [(0, 0), (1, 0), (1, 1), (2, 1)],

    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 1), (1, 0), (1, 1), (2, 0)]
]

case_num = 1

while True:
    n = int(input())
    if n == 0:
        break
     
    board = []
    for _ in range(n):
        board.append(list(map(int, input().split())))
    
    max_sum = float('-inf')
    
    for i in range(n):
        for j in range(n):
            for tetromino in tetrominos:
                current_sum = 0
                valid = True
                
                for dx, dy in tetromino:
                    nx, ny = i + dx, j + dy
                    
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        valid = False
                        break
                    
                    current_sum += board[nx][ny]
                
                if valid:
                    max_sum = max(max_sum, current_sum)
    
    print(f"{case_num}. {max_sum}")
    case_num += 1