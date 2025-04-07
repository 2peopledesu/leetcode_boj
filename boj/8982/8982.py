import sys
input = sys.stdin.readline

def initialize_water_tank():
    N = int(input())
    water_levels = []
    tank_depths = []
    
    prev_y = -1
    prev_x = -1
    
    for _ in range(N):
        x, y = map(int, input().split())
        
        if y == prev_y and prev_y != -1:
            for _ in range(x - prev_x):
                water_levels.append(prev_y)
                tank_depths.append(prev_y)
        
        prev_x, prev_y = x, y
    
    return water_levels, tank_depths

def initialize_holes():
    K = int(input())
    holes = []
    for _ in range(K):
        holes.append(list(map(int, input().split())))
    return holes

def simulate_water_drainage(tank_depths, water_levels, start_idx, end_idx, hole_y):

    for i in range(start_idx, end_idx):
        water_levels[i] = 0
    
    min_height = hole_y
    for i in range(start_idx-1, -1, -1):
        min_height = min(min_height, tank_depths[i])
        
        water_levels[i] = min(water_levels[i], tank_depths[i] - min_height)
    
    min_height = hole_y
    for i in range(end_idx, len(water_levels)):
        min_height = min(min_height, tank_depths[i])
        water_levels[i] = min(water_levels[i], tank_depths[i] - min_height)

def drain_all_holes(tank_depths, water_levels, holes):
    for start_x, hole_y, end_x, _ in holes:
        simulate_water_drainage(tank_depths, water_levels, start_x, end_x, hole_y)


water_levels, tank_depths = initialize_water_tank()
holes = initialize_holes()

drain_all_holes(tank_depths, water_levels, holes)

total_water = sum(water_levels)
print(total_water)

