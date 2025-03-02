import sys

input = sys.stdin.readline

n = int(input())
cranes = list(map(int, input().split()))
cranes.sort(reverse=True)

m = int(input())
boxes = list(map(int, input().split()))
boxes.sort(reverse=True)

if boxes[0] > cranes[0]:
    print(-1)
    sys.exit()

positions = [0] * n
moved = [False] * m

count = 0
moved_count = 0

while moved_count < m:
    count += 1
    
    for i in range(n):
        while positions[i] < m:
            # 아직 안 옮겨진 상자 중 현재 크레인이 들 수 있는 상자 찾기
            if not moved[positions[i]] and cranes[i] >= boxes[positions[i]]:
                moved[positions[i]] = True
                moved_count += 1
                break
            positions[i] += 1
    
            
print(count)