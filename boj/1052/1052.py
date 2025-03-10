import sys

input = sys.stdin.readline

n, k = map(int, input().split())

if n <= k:
    print(k - n)
    sys.exit()

if n == k:
    print(0)
    sys.exit()

