import sys

input = sys.stdin.readline

def check(s):
    cnt = [0] * 26
    jump = False
    for i in range(len(s)):
        if jump == True:
            jump = False
            continue
        cnt[ord(s[i]) - ord('A')] += 1
        if cnt[ord(s[i]) - ord('A')] == 3:
            if i == len(s) - 1 or s[i] != s[i + 1]:
                return False
            cnt[ord(s[i]) - ord('A')] = 0
            jump = True
    return True

n = int(input())

arr = [input().strip() for _ in range(n)]
for s in arr:
    print("OK" if check(s) else "FAKE")