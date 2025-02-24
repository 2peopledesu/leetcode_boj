import sys

input = sys.stdin.readline

while True:
    try:
        a, b = input().split()
        if not a: break
        
        a_index = 0
        found = False
        
        for char in b:
            if char == a[a_index]:
                a_index += 1
                if a_index == len(a):
                    found = True
                    break
        
        print("Yes" if found else "No")
        
    except:
        break