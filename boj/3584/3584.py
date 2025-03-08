import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    tree = {}
    
    n = int(input())
    
    for i in range(n - 1):
        parent, child = input().split()
        tree[child] = parent
    
    target1, target2 = input().split()
    
    target1_ancestors = []
    target2_ancestors = []
    
    while target1 in tree:
        target1_ancestors.append(target1)
        target1 = tree[target1]
        
    while target2 in tree:
        target2_ancestors.append(target2)
        target2 = tree[target2]
        
    target1_ancestors.append(target1)
    target2_ancestors.append(target2)
    
    ancestor_candidate = []
    
    for i, ancestor in enumerate(target1_ancestors):
        if ancestor in target2_ancestors:
            ancestor_candidate.append((ancestor, i + target2_ancestors.index(ancestor)))
    
    ancestor_candidate.sort(key=lambda x: x[1])
    
    print(ancestor_candidate[0][0])