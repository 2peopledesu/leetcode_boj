import sys

input = sys.stdin.readline

n = int(input())

mines = list(int(input()) for _ in range(n))

sorted_mines = sorted(enumerate(mines), key=lambda x: (-x[1], x[0]))

visited = [False] * n

result = []

for i, mine in sorted_mines:
    if visited[i]:
        continue
    
    visited[i] = True
    result.append(i + 1)
    
    left = i - 1
    now_mine = i
    while(left >= 0 and mines[left] < mines[now_mine]):
        if not visited[left]:
            visited[left] = True
        else:
            break
        left -= 1
        now_mine -= 1
        
    right = i + 1
    now_mine = i
    while(right < n and mines[right] < mines[now_mine]):
        if not visited[right]:
            visited[right] = True
        else:
            break
        right += 1
        now_mine += 1

result = sorted(result)

for i in result:
    print(i)