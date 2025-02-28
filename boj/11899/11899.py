import sys

input = sys.stdin.readline

n = input().strip()

stack = []

for elem in n:
    if elem == "(":
        stack.append(elem)
    else:
        if stack and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(elem)

print(len(stack))
