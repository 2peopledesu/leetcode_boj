import sys

input = sys.stdin.readline
count = 1
while True:
    n = int(input())
    if n == 0:
        break
    
    if count > 1:
        print()
        
    print(f"Group {count}")
    arr = [input().split() for _ in range(n)]
    
    flag = False
    
    for i in range(n):
        for j in range(1, n):
            if arr[i][j] == "N":
                flag = True
                nasty_index = (i - j) % n
                print(f"{arr[nasty_index][0]} was nasty about {arr[i][0]}")
    
    if not flag:
        print("Nobody was nasty")
        
    count += 1