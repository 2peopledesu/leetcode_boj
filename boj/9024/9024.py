import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = list(map(int, input().split()))
    
    s.sort()
    
    left = 0
    right = n - 1
    count = 0
    min_diff = float('inf')
    
    while left < right:
        diff = s[left] + s[right] - k
        
        if abs(diff) < min_diff:
            min_diff = abs(diff)
            count = 1
        elif abs(diff) == min_diff:
            count += 1
        
        if diff < 0:
            left += 1
        else:
            right -= 1
            
    print(count)