import sys

input = sys.stdin.readline

n = int(input())
first = input().strip()
count_first = [0] * 26

for c in first:
    count_first[ord(c) - ord('A')] += 1

result = 0

for _ in range(n-1):
    word = input().strip()
    count_word = [0] * 26
    
    for c in word:
        count_word[ord(c) - ord('A')] += 1
    
    total_diff = 0
    for i in range(26):
        total_diff += abs(count_first[i] - count_word[i])
    
    len_diff = abs(len(first) - len(word))
    
    if len_diff > 1:
        continue
    elif len_diff == 0:
        if total_diff <= 2:
            result += 1
    else:
        if total_diff == 1:
            result += 1

print(result)