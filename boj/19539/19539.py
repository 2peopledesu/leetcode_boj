import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
div3 = total // 3
if total % 3 != 0:
    print("NO")
    sys.exit()

count = 0
for elem in arr:
    count += elem // 2

if count >= div3:
    print("YES")
else:
    print("NO")