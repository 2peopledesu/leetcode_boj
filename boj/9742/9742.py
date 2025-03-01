import sys
import itertools

def find_nth_permutation(s, n):
    length = len(s)
    total = 1
    for i in range(1, length + 1):
        total *= i
    
    if n > total:
        return "No permutation"
    
    perms = itertools.permutations(s)
    for i, perm in enumerate(perms, 1):
        if i == n:
            return ''.join(perm)

while True:
    try:
        line = sys.stdin.readline().strip()
        if not line:
            break
            
        a, b = line.split()
        b = int(b)
        
        result = find_nth_permutation(a, b)
        print(f"{a} {b} = {result}")
            
    except EOFError:
        break