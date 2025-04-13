import sys

input = sys.stdin.readline

arr = []
for _ in range(9):
    row = list(map(int, input().strip()))
    arr.append(row)

empty_cells = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            empty_cells.append((i, j))

def check(i, j, num):
    for k in range(9):
        if arr[i][k] == num:
            return False

    for k in range(9):
        if arr[k][j] == num:
            return False
    
    start_row, start_col = (i // 3) * 3, (j // 3) * 3
    for k in range(start_row, start_row + 3):
        for l in range(start_col, start_col + 3):
            if arr[k][l] == num:
                return False
                
    return True

def solve(idx=0):
    if idx == len(empty_cells):
        return True
    
    i, j = empty_cells[idx]
    
    for num in range(1, 10):
        if check(i, j, num):
            arr[i][j] = num
            
            if solve(idx + 1):
                return True
            
            arr[i][j] = 0
    
    return False

solve()

for i in range(9):
    print(''.join(map(str, arr[i])))