import sys
from collections import deque

input = sys.stdin.readline

l = int(input())

m1, m2 = map(int, input().split()) # 기관총 사거리, 데미지
c = int(input()) # 지뢰 개수

zombies = [int(input()) for _ in range(l)]
reduction = 0

mine = deque()

for i in range(l):
    current_damage = m2 * min(i + 1, m1) - reduction
    if zombies[i] > current_damage:
        if c > 0:
            c -= 1
            reduction += m2
            mine.append(1)
        else:
            print("NO")
            exit(0)
    else:
        mine.append(0)
    
    if i >= m1:
        del_mine = mine.popleft()
        if del_mine == 1:
            reduction -= m2

print("YES")