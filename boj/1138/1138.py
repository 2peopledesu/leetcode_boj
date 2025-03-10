import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

result = [0] * (n)

for i in range(1, n + 1):
    count = 0
    for j in range(n):
        if result[j] == 0:
            if count == arr[i-1]:
                result[j] = i
                break
            count += 1

print(' '.join(map(str, result)))