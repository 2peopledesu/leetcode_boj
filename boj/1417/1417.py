import sys

input = sys.stdin.readline

n = int(input())
dasom_votes = int(input())

candidates = [int(input()) for _ in range(n - 1)]

count = 0

if n > 1:
    while True:
        max_votes = max(candidates)
        
        if dasom_votes > max_votes:
            break
        
        max_index = candidates.index(max_votes)
        candidates[max_index] -= 1
        dasom_votes += 1
        count += 1

print(count)