import sys

# 입력 받기
k = int(sys.stdin.readline())
x, y = map(int, sys.stdin.readline().split())
size = 2 ** k
board = [[0] * size for _ in range(size)]

# 하수구 위치 표시 (문제 좌표계를 배열 인덱스로 변환)
board[size - y][x - 1] = -1

# 타일 번호 (1, 2, 3, ...)
tile_num = 1

def fill_trominoes(board, r, c, size, hole_r, hole_c):
    global tile_num
    
    # 기저 사례: 크기가 2x2일 경우 직접 처리
    if size == 2:
        # 2x2 정사각형 내의 하수구 위치가 아닌 곳에 타일 채우기
        for i in range(r, r + 2):
            for j in range(c, c + 2):
                if board[i][j] == 0:  # 비어있는 칸이면
                    board[i][j] = tile_num
        tile_num += 1
        return
    
    # 분할된 크기
    new_size = size // 2
    
    # 하수구가 위치한 사분면 확인
    quad_r, quad_c = 0, 0
    if hole_r >= r + new_size: quad_r = 1
    if hole_c >= c + new_size: quad_c = 1
    
    # 중앙에 L-트로미노 놓기 (각 사분면에 하나씩 걸치도록)
    center_r, center_c = r + new_size - 1, c + new_size - 1
    
    for i in range(2):
        for j in range(2):
            if i == quad_r and j == quad_c:
                continue  # 하수구가 있는 사분면은 건너뛰기
            board[center_r + i][center_c + j] = tile_num
    
    tile_num += 1
    
    # 4개의 사분면으로 재귀 호출
    # 첫 번째 사분면 (왼쪽 위)
    if quad_r == 0 and quad_c == 0:
        fill_trominoes(board, r, c, new_size, hole_r, hole_c)
    else:
        fill_trominoes(board, r, c, new_size, center_r, center_c)
    
    # 두 번째 사분면 (오른쪽 위)
    if quad_r == 0 and quad_c == 1:
        fill_trominoes(board, r, c + new_size, new_size, hole_r, hole_c)
    else:
        fill_trominoes(board, r, c + new_size, new_size, center_r, center_c + 1)
    
    # 세 번째 사분면 (왼쪽 아래)
    if quad_r == 1 and quad_c == 0:
        fill_trominoes(board, r + new_size, c, new_size, hole_r, hole_c)
    else:
        fill_trominoes(board, r + new_size, c, new_size, center_r + 1, center_c)
    
    # 네 번째 사분면 (오른쪽 아래)
    if quad_r == 1 and quad_c == 1:
        fill_trominoes(board, r + new_size, c + new_size, new_size, hole_r, hole_c)
    else:
        fill_trominoes(board, r + new_size, c + new_size, new_size, center_r + 1, center_c + 1)

# 분할 정복으로 L-트로미노 채우기
hole_r, hole_c = size - y, x - 1  # 하수구 위치
fill_trominoes(board, 0, 0, size, hole_r, hole_c)

# 결과 출력
for i in range(size):
    print(' '.join(map(str, board[i])))