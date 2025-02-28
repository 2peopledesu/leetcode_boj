import sys
from itertools import combinations

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def get_max_distance(houses, shelters):
    max_dist = 0
    for house in houses:
        # 현재 집에서 가장 가까운 대피소까지의 거리
        if house in shelters:
            continue
        min_dist = float('inf')
        for shelter in shelters:
            dist = manhattan_distance(house[0], house[1], shelter[0], shelter[1])
            min_dist = min(min_dist, dist)
        max_dist = max(max_dist, min_dist)
    return max_dist

input = sys.stdin.readline

n, k = map(int, input().split())

house = list(list(map(int, input().split())) for _ in range(n))

comb = list(combinations(house, k))

result = sys.maxsize

for shleters in comb:
    result = min(result, get_max_distance(house, shleters))
    
print(result)