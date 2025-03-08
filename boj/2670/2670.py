import sys

input = sys.stdin.readline

n = int(input())

arr = [float(input()) for _ in range(n)]

arr2 = [0] * n

arr2[0] = arr[0]

for i in range(1, n):
    arr2[i] = max(arr[i], arr[i] * arr2[i - 1])
    
print("%.3f" % max(arr2))