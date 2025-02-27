import sys

input = sys.stdin.readline

k = int(input())
n = int(input())

final = list(input().strip())
start = [chr(i) for i in range(65, 65+k)]

ladder = []
for _ in range(n):
    ladder.append(list(input().strip()))

q_row = 0
for i in range(n):
    if '?' in ladder[i]:
        q_row = i
        break

top = start[:]
for i in range(q_row):
    for j in range(k-1):
        if ladder[i][j] == '-':
            top[j], top[j+1] = top[j+1], top[j]

bottom = final[:]
for i in range(n-1, q_row, -1):
    for j in range(k-1):
        if ladder[i][j] == '-':
            bottom[j], bottom[j+1] = bottom[j+1], bottom[j]

# ? 행에 들어갈 내용 결정
result = ['*'] * (k-1)
for i in range(k-1):
    if top[i] == bottom[i]:
        result[i] = '*'
    elif top[i] == bottom[i+1] and top[i+1] == bottom[i]:
        result[i] = '-'
        # 사다리를 놓았으면 교환
        top[i], top[i+1] = top[i+1], top[i]
    else:
        print('x' * (k-1))
        exit()

if top == bottom:
    print(''.join(result))
else:
    print('x' * (k-1))