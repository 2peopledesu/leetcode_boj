import sys
from collections import defaultdict

input = sys.stdin.readline

# 물고기 수와 시뮬레이션 횟수 입력
fish_count, simulation_count = map(int, input().split())
smell_map = [[0] * 5 for _ in range(5)]  # 상어 냄새를 저장하는 맵

# 8방향 이동 벡터 (1번부터 8번까지, 반시계 방향)
fish_dy = ('_', 0, -1, -1, -1, 0, 1, 1, 1)
fish_dx = ('_', -1, -1, 0, 1, 1, 1, 0, -1)

# 4방향 이동 벡터 (상, 좌, 하, 우)
shark_dy = ('_', -1, 0, 1, 0)
shark_dx = ('_', 0, -1, 0, 1)

# 물고기 정보 저장 구조
fish_positions = defaultdict(list)  # 현재 물고기 위치와 방향
temp_fish_positions = defaultdict(list)  # 이동 후 물고기 위치와 방향

# 초기 물고기 정보 입력
for i in range(fish_count):
    y, x, direction = tuple(map(int, input().split()))
    fish_positions[(y, x)].append(direction)

# 상어 초기 위치 입력
shark_position = tuple(map(int, input().split()))

def is_invalid_position(y, x):
    """격자 범위를 벗어나는지 확인하는 함수"""
    return y < 1 or x < 1 or y > 4 or x > 4

def move_fishes():
    """모든 물고기를 이동시키는 함수"""
    global temp_fish_positions
    
    for position, directions in fish_positions.items():
        y, x = position
        for direction in directions:
            can_move = False
            current_direction = direction
            
            # 8방향 검사 (최대 8번)
            for i in range(8):
                ny = y + fish_dy[current_direction]
                nx = x + fish_dx[current_direction]
                
                # 격자 밖이거나, 상어가 있거나, 냄새가 있으면 이동 불가
                if (is_invalid_position(ny, nx) or 
                    (ny, nx) == shark_position or 
                    smell_map[ny][nx] > 0):
                    # 반시계 방향으로 45도 회전
                    current_direction = current_direction - 1 if current_direction != 1 else 8
                    continue
                else:
                    # 이동 가능한 경우
                    can_move = True
                    temp_fish_positions[(ny, nx)].append(current_direction)
                    break
            
            # 이동할 수 없는 경우, 제자리에 머물기
            if not can_move:
                temp_fish_positions[(y, x)].append(direction)

def find_best_shark_path(current_position, path_so_far, fish_eaten_count, visited_positions):
    """상어의 최적 이동 경로를 찾는 함수"""
    global best_shark_path
    
    # 경로가 있고, 현재 위치를 아직 방문하지 않았다면 물고기를 먹는다
    if len(path_so_far) != 0:
        if current_position not in visited_positions:
            fish_eaten_count += len(temp_fish_positions[current_position])
            visited_positions.append(current_position)
    
    # 3칸 이동 완료 시, 최적 경로인지 확인
    if len(path_so_far) == 3:
        if best_shark_path is None:
            best_shark_path = (int(path_so_far), current_position, fish_eaten_count, visited_positions)
        # 더 많은 물고기를 먹거나, 같은 수의 물고기를 먹었지만 사전순으로 더 앞선 경로
        elif (best_shark_path[2] < fish_eaten_count or 
              (best_shark_path[2] == fish_eaten_count and best_shark_path[0] > int(path_so_far))):
            best_shark_path = (int(path_so_far), current_position, fish_eaten_count, visited_positions)
        return
    
    # 상하좌우 네 방향으로 탐색
    for direction in range(1, 5):
        y, x = current_position
        ny = y + shark_dy[direction]
        nx = x + shark_dx[direction]
        
        # 격자 내부인 경우만 이동
        if not is_invalid_position(ny, nx):
            find_best_shark_path((ny, nx), path_so_far + str(direction), 
                              fish_eaten_count, visited_positions.copy())

def process_shark_movement():
    """상어가 이동하며 물고기를 먹고 냄새를 남기는 함수"""
    global fish_positions, temp_fish_positions, shark_position, best_shark_path
    
    # 최적 경로 정보 추출
    _, new_shark_position, _, eaten_positions = best_shark_path
    shark_position = new_shark_position
    
    # 경로 상의 물고기 먹기 및 냄새 남기기
    for position in eaten_positions:
        y, x = position
        if temp_fish_positions[position]:
            smell_map[y][x] = 3  # 3턴 동안 냄새 유지
            temp_fish_positions.pop(position)
    
    # 냄새 감소시키기
    for y in range(1, 5):
        for x in range(1, 5):
            if smell_map[y][x] > 0:
                smell_map[y][x] -= 1
    
    for position, directions in temp_fish_positions.items():
        if directions:
            fish_positions[position].extend(directions)
    
    temp_fish_positions = defaultdict(list)

# 시뮬레이션 실행
for i in range(simulation_count):
    move_fishes()
    
    best_shark_path = None
    find_best_shark_path(shark_position, '', 0, [])
    
    process_shark_movement()

# 남은 물고기 수 계산
total_fish_count = 0
for directions in fish_positions.values():
    total_fish_count += len(directions)
print(total_fish_count)