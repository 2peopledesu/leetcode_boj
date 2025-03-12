import sys

input = sys.stdin.readline

def solution(skyline_points):
    stack = [0]
    building_count = 0
    
    for _, height in skyline_points:
        while stack[-1] > height:
            if stack[-1] > 0:
                building_count += 1
            stack.pop()
        
        if stack[-1] < height:
            stack.append(height)
    
    while stack[-1] > 0:
        building_count += 1
        stack.pop()
    
    return building_count

n = int(input())
skyline_points = []

for _ in range(n):
    x, y = map(int, input().split())
    skyline_points.append((x, y))

skyline_points.sort()
print(solution(skyline_points))