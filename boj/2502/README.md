# 2502 떡 먹는 호랑이

## Problem Link

https://www.acmicpc.net/problem/2502

## Solution

```python
import sys

input = sys.stdin.readline

D, K = map(int, input().split())

dp = [0 for _ in range(D)]

dp[0], dp[1] = 1, 1

while(1):
    for i in range(2, D):
        dp[i] = dp[i - 2] + dp[i - 1]

    if dp[D - 1] == K:
        print(dp[0])
        print(dp[1])
        break

    if dp[D - 1] > K:
        dp[0] += 1
        dp[1] = dp[0]
    else:
        dp[1] += 1
```

## Explanation

This solution uses dynamic programming to find the first and second day's rice cake quantities. Here's how it works:

1. We start with initial values of 1 for both first and second days
2. Using Fibonacci-like sequence, we calculate subsequent days' values
3. If the final day's value matches K:
   - We've found our answer
   - Print the first and second day's values
4. If the final day's value is greater than K:
   - Reset by incrementing first day's value
   - Set second day's value equal to first day's
5. If the final day's value is less than K:
   - Increment second day's value and continue
