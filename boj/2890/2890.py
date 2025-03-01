import sys

input = sys.stdin.readline

r, c = map(int, input().split())

board = [list(input().strip()) for _ in range(r)]

medal = [0] * 9

count = 0

for i in range(c - 1, 0, -1):
    flag = True
    for j in range(r):
        if board[j][i] in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            if medal[int(board[j][i]) - 1] == 0:
                if flag:
                    count += 1
                    flag = False
                medal[(int(board[j][i])) - 1] = count

for elem in medal:
    print(elem)