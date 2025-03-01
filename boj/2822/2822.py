import sys

scores = [(int(sys.stdin.readline()), i+1) for i in range(8)]

scores.sort(reverse=True)

total = sum(score for score, _ in scores[:5])

selected = sorted(idx for _, idx in scores[:5])

print(total)
print(' '.join(map(str, selected)))