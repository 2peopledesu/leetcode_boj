from collections import defaultdict
import sys
sys.setrecursionlimit(10**6)

def dfs(node, depth):
    visited[node] = depth
    
    for next_node in sorted(nodes[node]):
        if visited[next_node] == -1:
            dfs(next_node, depth + 1)

input = sys.stdin.readline

n, m, r = map(int, input().split())

nodes = defaultdict(list)

visited = [-1] * (n + 1)

for i in range(m):
    u, v = map(int, input().split())
        
    nodes[u].append(v)
    nodes[v].append(u)

dfs(r, 0)

for i in range(1, n + 1):
    print(visited[i])
    