import sys
import bisect

input = sys.stdin.readline

n, m = map(int, input().split())
A = [int(input()) for _ in range(n)]
B = sorted(A)

first_occurrence = {}
for idx, num in enumerate(B):
    if num not in first_occurrence:
        first_occurrence[num] = idx

for _ in range(m):
    D = int(input())
    pos = bisect.bisect_left(B, D)
    if pos < n and B[pos] == D:
        print(first_occurrence[D])
    else:
        print(-1)