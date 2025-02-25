# 1904 01타일

## Problem Link

https://www.acmicpc.net/problem/1904

## Solution

This problem uses dynamic programming to calculate the number of possible binary tile arrangements.

Key Logic:

1. Base Cases:

   - For N = 1: Only one possible arrangement (1)
   - For N = 2: Two possible arrangements (00, 11)
   - For N = 3: Three possible arrangements (001, 100, 111)

2. Dynamic Programming:

   - Uses the recurrence relation: dp[i] = dp[i-1] + dp[i-2]
   - Each state represents number of possible arrangements for length i
   - Similar to Fibonacci sequence pattern
   - Takes modulo 15746 at each step to prevent overflow

3. Pattern Explanation:
   - For any position i, we can either:
     - Add "1" to all arrangements of length i-1
     - Add "00" to all arrangements of length i-2

Time Complexity: O(N), where N is the input number.
Space Complexity: O(N) to store the dp array.
