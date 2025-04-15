import sys

input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

n, m = len(s1), len(s2)
max_length = min(n, m)

def solution():
    for length in range(max_length, 0, -1):
        hash_set = set()
        
        for i in range(n - length + 1):
            freq = [0] * 26
            for j in range(length):
                freq[ord(s1[i+j]) - ord('a')] += 1
            
            hash_set.add(tuple(freq))
        
        for i in range(m - length + 1):
            freq = [0] * 26
            for j in range(length):
                freq[ord(s2[i+j]) - ord('a')] += 1
            
            if tuple(freq) in hash_set:
                return length
    return 0
result = solution()
print(result)