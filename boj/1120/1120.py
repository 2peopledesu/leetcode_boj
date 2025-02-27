import sys

input = sys.stdin.readline

input_line = input().rstrip()

input1, input2 = input_line.split()

result = []

for i in range(len(input2) - len(input1) + 1):
    count = 0
    for j in range(len(input1)):
        if input1[j] != input2[i+j]:
            count += 1
    result.append(count)
    
print(min(result))