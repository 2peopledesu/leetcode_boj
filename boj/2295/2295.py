import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())

u = list(int(input()) for _ in range(n))

sum_ab = set()
for a in u:
    for b in u:
        sum_ab.add(a + b)

for d in reversed(u):
    for c in u:
        if (d - c) in sum_ab:
            print(d)
            sys.exit()