import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

del_target = int(input())

tree = {}

for index, elem in enumerate(arr):
    if elem == -1:
        root = index
    else:
        if elem not in tree:
            tree[elem] = []
        tree[elem].append(index)

if root == del_target:
    print(0)
    exit()

def dfs(node):
    if node == del_target:
        return 0
    if node not in tree:
        return 1
    leaf = 0
    for child in tree[node]:
        leaf += dfs(child)
    if leaf == 0:
        return 1
    return leaf

print(dfs(root))