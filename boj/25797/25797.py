import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
chocolate = [[0] * n for _ in range(n)]

for _ in range(k):
    r, c, s = map(int, input().split())
    chocolate[r - 1][c - 1] = s
    
ascii_board = [list(input().strip()) for _ in range(2 * n + 1)]

horizontal_walls = [[False] * n for _ in range(n+1)]
vertical_walls = [[False] * (n+1) for _ in range(n)]

for i in range(2*n+1):
    for j in range(2*n+1):
        if i % 2 == 0 and j % 2 == 1 and j < 2*n:
            horizontal_walls[i//2][j//2] = (ascii_board[i][j] == '-')
        elif i % 2 == 1 and j % 2 == 0 and i < 2*n:
            vertical_walls[i//2][j//2] = (ascii_board[i][j] == '|')

def extract_area():
    areas = [[0] * n for _ in range(n)]
    count = 0
    
    for i in range(n):
        for j in range(n):
            if areas[i][j] == 0:
                count += 1
                q = deque([(i, j)])
                areas[i][j] = count
                
                while q:
                    x, y = q.popleft()
                    
                    if y+1 < n and areas[x][y+1] == 0 and not vertical_walls[x][y+1]:
                        areas[x][y+1] = count
                        q.append((x, y+1))
                    
                    if x+1 < n and areas[x+1][y] == 0 and not horizontal_walls[x+1][y]:
                        areas[x+1][y] = count
                        q.append((x+1, y))
                    
                    if y-1 >= 0 and areas[x][y-1] == 0 and not vertical_walls[x][y]:
                        areas[x][y-1] = count
                        q.append((x, y-1))
                    
                    if x-1 >= 0 and areas[x-1][y] == 0 and not horizontal_walls[x][y]:
                        areas[x-1][y] = count
                        q.append((x-1, y))
    
    return areas, count

def find_color_area(areas, area_count):
    white_areas = []
    grey_areas = []
    
    for color in [0, 1]:
        visited = [[False] * n for _ in range(n)]
        
        for i in range(n):
            for j in range(n):
                if board[i][j] == color and areas[i][j] == area_count and not visited[i][j]:
                    area = []
                    q = deque([(i, j)])
                    visited[i][j] = True
                    
                    while q:
                        x, y = q.popleft()
                        area.append((x, y))
                        
                        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                            nx, ny = x + dx, y + dy
                            if (0 <= nx < n and 0 <= ny < n and 
                                board[nx][ny] == color and areas[nx][ny] == area_count and 
                                not visited[nx][ny]):
                                visited[nx][ny] = True
                                q.append((nx, ny))
                    
                    if color == 0:
                        white_areas.append(area)
                    else:
                        grey_areas.append(area)
    
    return white_areas, grey_areas

def check_area(white_area, grey_area):
    if len(white_area) != len(grey_area):
        return False
    
    def normalize(area):
        min_x = min(x for x, y in area)
        min_y = min(y for x, y in area)
        return sorted([(x - min_x, y - min_y) for x, y in area])
    
    def rotate90(points):
        return [(y, -x) for x, y in points]
    
    def flip_horizontal(points):
        return [(x, -y) for x, y in points]
    
    def flip_vertical(points):
        return [(-x, y) for x, y in points]
    
    def flip_diagonal(points):
        return [(y, x) for x, y in points]
    
    def flip_anti_diagonal(points):
        return [(-y, -x) for x, y in points]
    
    normalized_white = set(normalize(white_area))
    normalized_grey = normalize(grey_area)
    
    if set(normalized_grey) == normalized_white:
        return True
    
    rot90 = normalize(rotate90(normalized_grey))
    if set(rot90) == normalized_white:
        return True
    
    rot180 = normalize(rotate90(rot90))
    if set(rot180) == normalized_white:
        return True
    
    rot270 = normalize(rotate90(rot180))
    if set(rot270) == normalized_white:
        return True
    
    flip_h = normalize(flip_horizontal(normalized_grey))
    if set(flip_h) == normalized_white:
        return True
    
    flip_v = normalize(flip_vertical(normalized_grey))
    if set(flip_v) == normalized_white:
        return True
    
    flip_d = normalize(flip_diagonal(normalized_grey))
    if set(flip_d) == normalized_white:
        return True
    
    flip_ad = normalize(flip_anti_diagonal(normalized_grey))
    if set(flip_ad) == normalized_white:
        return True
    
    return False

def check_board():
    areas, count = extract_area()
    
    for i in range(n):
        for j in range(n):
            if j+1 < n and areas[i][j] == areas[i][j+1]:
                if vertical_walls[i][j+1]:
                    return False
            
            if i+1 < n and areas[i][j] == areas[i+1][j]:
                if horizontal_walls[i+1][j]:
                    return False
    
    for area_count in range(1, count + 1):
        white_areas, grey_areas = find_color_area(areas, area_count)
        
        if len(white_areas) != 1 or len(grey_areas) != 1:
            return False
        
        white_area = white_areas[0]
        grey_area = grey_areas[0]
        
        if not check_area(white_area, grey_area):
            return False
        
        check_numbers_in_area = []
        for x, y in white_area + grey_area:
            if chocolate[x][y] != 0:
                check_numbers_in_area.append((x, y, chocolate[x][y]))
        
        if len(check_numbers_in_area) > 1:
            return False
        
        if check_numbers_in_area:
            x, y, number = check_numbers_in_area[0]
            if len(white_area) != number or len(grey_area) != number:
                return False
    
    return True

if check_board():
    print(1)
else:
    print(0)