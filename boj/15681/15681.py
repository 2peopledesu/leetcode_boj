import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

n, r, q = map(int, input().split())

tree = defaultdict(list)

for _ in range(n - 1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
    
children = defaultdict(list)

def make_tree(node, parent):
    for child in tree[node]:
        if child != parent:
            children[node].append(child)
            make_tree(child, node)
            
subtree_size = [0] * (n + 1)

def count_subtree_size(node, parent):
    subtree_size[node] = 1
    for child in children[node]:
        if child != parent:
            count_subtree_size(child, node)
            subtree_size[node] += subtree_size[child]

make_tree(r, -1)
count_subtree_size(r, -1)

for _ in range(q):
    a = int(input())
    print(subtree_size[a])