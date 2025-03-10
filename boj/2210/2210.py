import sys

def recursion(x, y, num, cnt):
    if cnt == 6:
        if num not in result:
            result.add(num)
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            recursion(nx, ny, num * 10 + board[nx][ny], cnt + 1)

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]

result = set()

dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]


for i in range(5):
    for j in range(5):
        recursion(i, j, board[i][j], 1)
        
print(len(result))