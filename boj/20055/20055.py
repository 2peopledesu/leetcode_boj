import sys

input = sys.stdin.readline

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0] * n

empty = 0
step = 0

while empty < k:
    step += 1
    
    belt = [belt[-1]] + belt[:-1]
    robot = [0] + robot[:-1]
    robot[n-1] = 0  
    
    for i in range(n-2, -1, -1):
        if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
            robot[i] = 0
            robot[i+1] = 1
            belt[i+1] -= 1
            if belt[i+1] == 0:
                empty += 1
    robot[n-1] = 0  
    
    if belt[0] > 0:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            empty += 1

print(step)

