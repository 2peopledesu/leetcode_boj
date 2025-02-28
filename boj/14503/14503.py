import sys

input = sys.stdin.readline

dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

n, m = map(int, input().split())

# r, c = start point, d = 북 동 남 서 
r, c, d = map(int, input().split())

# 0 == need to clean, 1 == wall
room = list(list(map(int, input().split())) for _ in range(n))

count = 0

def is_array(x, y):
    return n > x >= 0 and m > y >= 0

def clean_now_point(x, y):
    return room[x][y] == 0

while(1):
    if clean_now_point(r, c):
        count += 1
        room[r][c] = 2
    
    for i in range(4):
        next_x = r + dxs[i]
        next_y = c + dys[i]
        
        flag = True
        if is_array(next_x, next_y):
            if room[next_x][next_y] == 0:
                flag = False
                d = (d + 3) % 4
                if is_array(r + dxs[d], c + dys[d]):
                    if room[r + dxs[d]][c + dys[d]] == 0:
                        r = r + dxs[d]
                        c = c + dys[d]
                        break
                break
    if flag:
        if is_array(r + dxs[(d + 2) % 4], c + dys[(d + 2) % 4]):
            if room[r + dxs[(d + 2) % 4]][c + dys[(d + 2) % 4]] == 1:
                break
            else:
                r = r + dxs[(d + 2) % 4]
                c = c + dys[(d + 2) % 4]

print(count)