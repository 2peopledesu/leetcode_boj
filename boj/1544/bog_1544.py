import sys

def is_cyclic(a, b):
    if len(a) != len(b):
        return False
    return a in (b + b)

input = sys.stdin.readline

n = int(input())
arr = [input().strip() for _ in range(n)]
arr.sort(key=lambda x: len(x))
visit = [0] * n
group = 0

for i in range(n):
    if visit[i] == 0:
        group += 1
        visit[i] = group
        current = arr[i]
        current_len = len(current)
        for j in range(i + 1, n):
            if visit[j] == 0 and len(arr[j]) == current_len:
                if is_cyclic(current, arr[j]):
                    visit[j] = group

print(group)