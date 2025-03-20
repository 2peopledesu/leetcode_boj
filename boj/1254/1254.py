def is_palindrome(s):
    return s == s[::-1]

def solution(s):
    n = len(s)
    
    if is_palindrome(s):
        return n
    
    for i in range(n):
        if is_palindrome(s[i:]):
            return n + i
    
    return n * 2 - 1

s = input().strip()
print(solution(s))