import sys

input = sys.stdin.readline

n = int(input())
words = []
for i in range(n):
    words.append(input().rstrip())

max_len = 0
ans1, ans2 = 0, 1

prefix_dict = {}
for i in range(n):
    word = words[i]
    for j in range(1, len(word) + 1):
        prefix = word[:j]
        if prefix not in prefix_dict:
            prefix_dict[prefix] = []
        if len(prefix_dict[prefix]) < 2:
            prefix_dict[prefix].append(i)

for prefix, indices in prefix_dict.items():
    if len(indices) == 2:
        prefix_len = len(prefix)
        if prefix_len > max_len:
            max_len = prefix_len
            ans1, ans2 = indices
        elif prefix_len == max_len:
            if indices[0] < ans1 or (indices[0] == ans1 and indices[1] < ans2):
                ans1, ans2 = indices

print(words[ans1])
print(words[ans2])