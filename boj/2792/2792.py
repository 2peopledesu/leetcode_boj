import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(m)]

left = 1
right = max(arr)

while(left < right):
    mid = (left + right) // 2
    student = 0
    for elem in arr:
        student += (elem + mid - 1) // mid
    
    if student <= n:
        right = mid
    elif student > n:
        left = mid + 1

print(left)