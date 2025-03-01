import sys

input = sys.stdin.readline

n = int(input())

arr = list(int(input()) for _ in range(n))

arr = sorted(arr)

result = 0

for i in range(1, n + 1):
    result += abs(arr[i - 1] - i)
    
print(result)