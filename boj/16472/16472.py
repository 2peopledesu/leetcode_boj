import sys
from collections import defaultdict

n = int(sys.stdin.readline())
cat_say = sys.stdin.readline().strip()
max_len = 0
char_count = defaultdict(int)
left = 0

for right in range(len(cat_say)):
    char = cat_say[right]
    char_count[char] += 1

    while len(char_count) > n:
        left_char = cat_say[left]
        char_count[left_char] -= 1
        if char_count[left_char] == 0:
            del char_count[left_char]
        left += 1

    max_len = max(max_len, right - left + 1)

print(max_len)