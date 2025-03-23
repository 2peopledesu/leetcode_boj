import sys

input = sys.stdin.readline

s = input().strip()
max_len = len(s)
visited = set()
result = []

def backtrack(index, current, max_num):
    if index == max_len:
        if all(i in visited for i in range(1, max_num + 1)):
            print(' '.join(current))
            exit()
        return

    num = int(s[index])
    if num not in visited and num != 0:
        visited.add(num)
        backtrack(index + 1, current + [str(num)], max(max_num, num))
        visited.remove(num)

    if index + 1 < max_len:
        num = int(s[index:index+2])
        if num not in visited and 1 <= num <= 50:
            visited.add(num)
            backtrack(index + 2, current + [str(num)], max(max_num, num))
            visited.remove(num)

backtrack(0, [], 0)