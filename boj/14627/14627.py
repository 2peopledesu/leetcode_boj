import sys

input = sys.stdin.readline

s, c = map(int, input().split())
onion = list(int(input()) for _ in range(s))

left = 1
right = sum(onion) // c

while(left <= right):
    mid = (left + right) // 2
    count = 0
    for elem in onion:
        count += elem // mid
    
    if count >= c:
        left = mid + 1
    else:
        right = mid - 1

result = 0

print(sum(onion) - (right * c))