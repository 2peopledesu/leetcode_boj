import sys
from collections import deque

input = sys.stdin.readline

def bfs(a, b):
    q = deque([a])
    visited[ord(a) - ord('a')] = True
    
    while q:
        next_target = q.popleft()
        for elem in arr[ord(next_target) - ord('a')]:
            if elem and not visited[ord(elem) - ord('a')]:
                visited[ord(elem) - ord('a')] = True
                q.append(elem)
                if elem == b:
                    return 'T'
    return 'F'

n = int(input())

arr = [[] for _ in range(26)]

for i in range(n):
    a, b = input().strip().split(' is ')
    arr[ord(a) - ord('a')].append(b)
    
m = int(input())

for i in range(m):
    a, b = input().strip().split(' is ')
    visited = [False] * 26
    print(bfs(a, b))
