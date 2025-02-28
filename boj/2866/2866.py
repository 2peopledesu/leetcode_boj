import sys

input = sys.stdin.readline

r, c = map(int, input().split())

table = list(list(input().strip()) for _ in range(r))

left = 0
right = r - 1

while(left <= right):
    mid = (left + right) // 2
    check = set()
    
    flag = True
    
    for i in range(c):
        sumchr = ""
        for j in range(mid, r):
            sumchr += table[j][i]
        if sumchr in check:
            flag = False
            break
        else:
            check.add(sumchr)
    if flag:
        left = mid + 1
    else:
        right = mid - 1

print(right)