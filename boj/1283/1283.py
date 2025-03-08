import sys

input = sys.stdin.readline

n = int(input())

dict = {}

for i in range(n):
    words = input().split()
    flag = False
    for j in range(len(words)):
        if not flag:
            if words[j][0].lower() not in dict:
                dict[words[j][0].lower()] = words[j]
                words[j] = '[' + words[j][0] + ']' + words[j][1:]
                flag = True
                break
    if not flag:
        for j in range(len(words)):
            if not flag:
                for k in range(1, len(words[j])):
                    if words[j][k].lower() not in dict:
                        dict[words[j][k].lower()] = words[j]
                        words[j] = words[j][:k] + '[' + words[j][k] + ']' + words[j][k+1:]
                        flag = True
                        break
                
    print(' '.join(words))
    