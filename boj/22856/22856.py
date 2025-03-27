import sys
from collections import defaultdict

def find_last_inorder():
    last = None
    
    def inorder(node):
        nonlocal last
        if node == -1:
            return
        
        inorder(left[node])
        last = node
        inorder(right[node])
    
    inorder(1)
    return last

def count_depth(last_node):
    depth = 0
    current_node = last_node
    
    while current_node != 1:
        depth += 1
        current_node = parent[current_node]
        
    return depth

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

left = defaultdict(lambda: -1)
right = defaultdict(lambda: -1)
parent = {1: -1}

for _ in range(n):
    a, b, c = map(int, input().split())
    left[a] = b
    right[a] = c
    
    if b != -1:
        parent[b] = a
    if c != -1:
        parent[c] = a
        
edge = n - 1
last_node = find_last_inorder()
depth = count_depth(last_node)

print(2 * edge - depth)