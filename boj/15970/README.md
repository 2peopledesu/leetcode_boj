# 15970 화살표 그리기

## Problem Link

https://www.acmicpc.net/problem/15970

## Solution

```python3
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
```

## Explanation

First, I sort the points by color to group same-colored points together. Then, for each point, I search for points of the same color on both sides. The logic follows these steps:

1. If a point has the same color on both sides, I calculate distances to both points and choose the shorter one
2. If a point has the same color on only one side, I use that distance
3. I add the chosen minimum distance to our result

Since point positions can go up to 10^5, sorting the points first is crucial as it allows us to only calculate distances between adjacent points of the same color, making the solution more efficient.
