import sys

input = sys.stdin.readline

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort(key=lambda x: (x[1], x[0]))

result = 0

for i in range(n):
    target_num = None
    current_color = arr[i][1]
    
    if i + 1 < n and arr[i + 1][1] == current_color:
        target_num = i + 1
        
    if i - 1 >= 0 and arr[i - 1][1] == current_color:
        if target_num is None:
            target_num = i - 1
        else:
            if abs(arr[i][0] - arr[i - 1][0]) < abs(arr[i][0] - arr[target_num][0]):
                target_num = i - 1

    if target_num is not None:
        result += abs(arr[i][0] - arr[target_num][0])

print(result)
