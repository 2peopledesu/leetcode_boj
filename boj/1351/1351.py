import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

def dfs(x):
    if x in dp:
        return dp[x]
    dp[x] = dfs(x // p) + dfs(x // q)
    return dp[x]

input = sys.stdin.readline

n, p, q = map(int, input().split())

dp = defaultdict(int)
dp[0] = 1

print(dfs(n))