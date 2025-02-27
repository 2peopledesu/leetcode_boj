import sys

input = sys.stdin.readline

n = input().rstrip()
target = input().rstrip()

jump = 0
result = 0
check = ""

for i in range(len(n)):
    if(jump != 0):
        jump -= 1
        continue
    if n[i] == target[0]:
        if (i + len(target) <= len(n)):
            for j in range(i, i + len(target)):
                check += n[j]
            if check == target:
                result += 1
                jump = len(target) - 1
            check = ""

print(result)