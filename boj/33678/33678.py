import sys

input = sys.stdin.readline

n, k, x = map(int, input().split())
 
income = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)

for i in range(n):
    prefix_sum[i+1] = prefix_sum[i] + income[i]

left, right = 1, n
max_vacation = -1

max_income = sum(income) * x

if max_income < k:
    print(-1)
    sys.exit()

def possible_check(day):
    if day >= n:
        return False
    
    if day < 0:
        return False
    
    for start in range(n - day + 1):
        end = start + day
        
        before = prefix_sum[start] * x
        
        after = prefix_sum[n] - prefix_sum[end]
        
        total_income = before + after
        
        if total_income >= k:
            return True
        
    return False

while left <= right:
    mid = (left + right) // 2
    
    if possible_check(mid):
        max_vacation = mid
        left = mid + 1
    else:
        right = mid - 1

print(max_vacation if max_vacation != -1 else -1)