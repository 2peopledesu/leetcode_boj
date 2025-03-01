import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = list(input().strip() for _ in range(n))


visited = [[False] * m for _ in range(n)]

count = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            visited[i][j] = True
            if arr[i][j] == '-':
                for k in range(j + 1, m):
                    if arr[i][k] == '-':
                        visited[i][k] = True
                    else:
                        break
            if arr[i][j] == "|":
                for k in range(i + 1, n):
                    if arr[k][j] == "|":
                        visited[k][j] = True
                    else:
                        break
            
            count += 1

print(count)