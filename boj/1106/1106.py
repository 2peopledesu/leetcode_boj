import sys

input = sys.stdin.readline

def solution():
    C, N = map(int, input().split())
    
    dp = [float('inf')] * (C + 100)
    dp[0] = 0
    
    cities = []
    for _ in range(N):
        cost, customers = map(int, input().split())
        cities.append((cost, customers))
    
    for cost, customers in cities:
        for i in range(C + 100):
            if i + customers < C + 100:
                dp[i + customers] = min(dp[i + customers], dp[i] + cost)
    
    return min(dp[C:])

print(solution())