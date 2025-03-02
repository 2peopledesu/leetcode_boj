import sys

input = sys.stdin.readline

n, m = map(int, input().split())

train = list([0] * 20 for _ in range(n))
can_pass = set()

for i in range(m):
    order = input().split()
    x = int(order[0])
    target_train = int(order[1]) - 1
    
    if x == 1:
        target_seat = int(order[2]) - 1
        train[target_train][target_seat] = 1
    elif x == 2:
        target_seat = int(order[2]) - 1
        train[target_train][target_seat] = 0
    elif x == 3:
        for j in range(19, 0, -1):
            train[target_train][j] = train[target_train][j-1]
        train[target_train][0] = 0
    elif x == 4:
        for j in range(0, 19):
            train[target_train][j] = train[target_train][j+1]
        train[target_train][19] = 0

unique_trains = set(tuple(train[i]) for i in range(n))
print(len(unique_trains))