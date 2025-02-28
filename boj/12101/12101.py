import sys

input = sys.stdin.readline

def recursive(now_list):
    if sum(now_list) == n:
        available.append(now_list[:])
        return
    if sum(now_list) > n:
        return
    
    for i in range(1, 4):
        now_list.append(i)
        recursive(now_list)
        now_list.pop()

n, k = map(int, input().split())
available = []
recursive([]) 

if len(available) < k:
    print(-1)
else:
    print('+'.join(map(str, available[k-1])))