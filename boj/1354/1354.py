import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(k):
    if k < 0:
        return 1
    if k in dp:
        return dp[k]
    
    dp[k] = dfs((k // p) - x) + dfs((k // q) - y)
    return dp[k]

input = sys.stdin.readline

n, p, q, x, y = map(int, input().split())

dp = defaultdict(int)
dp[0] = 1

print(dfs(n))