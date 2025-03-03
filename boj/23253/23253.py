import sys

input = sys.stdin.readline

n, m = map(int, input().split())

possible = True

for i in range(m):
    k = int(input())
    books = list(map(int, input().split()))
    for j in range(k-1):
        if books[j] < books[j+1]:
            possible = False
            break
    
    if not possible:
        break

print("Yes" if possible else "No")  