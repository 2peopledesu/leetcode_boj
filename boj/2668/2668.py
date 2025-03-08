import sys

input = sys.stdin.readline

n = int(input())
arr = [0] * (n + 1)
for i in range(1, n + 1):
    arr[i] = int(input())

visited = [False] * (n + 1)
result = set()

for i in range(1, n + 1):
    if not visited[i]:
        path = []
        current = i
        while True:
            if visited[current]:
                if current in path:
                    idx = path.index(current)
                    cycle = path[idx:]
                    for num in cycle:
                        result.add(num)
                break
            visited[current] = True
            path.append(current)
            current = arr[current]

sorted_result = sorted(result)
print(len(sorted_result))
for num in sorted_result:
    print(num)