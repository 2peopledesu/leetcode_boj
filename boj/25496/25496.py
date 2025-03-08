import sys

input = sys.stdin.readline

p, n = map(int, input().split())

arr = list(map(int, input().split()))

arr = sorted(arr)

count = 0

while(p < 200):
    p += arr[count]
    count += 1
    
print(count)