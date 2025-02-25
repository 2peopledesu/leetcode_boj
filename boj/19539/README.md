# 19539 사과나무

## Problem Link

https://www.acmicpc.net/problem/19539

## Solution

This problem determines if it's possible to grow trees to specific heights using two types of watering cans (growth +1 and +2).

Key Logic:

1. Total Sum Check:

   - Sum of all target heights must be divisible by 3
   - Because each operation (using both watering cans) adds 3 to total height
   - If not divisible by 3, it's impossible ("NO")

2. Growth Pattern Analysis:

   - Count how many times we can use the +2 watering can (elem // 2)
   - We need at least total/3 uses of +2 watering can
   - Because each complete operation needs one +2 and one +1

3. Final Verification:
   - If count of possible +2 operations >= total/3
   - Then we can arrange the watering operations to achieve target heights
   - Otherwise, it's impossible

Time Complexity: O(N), where N is the number of trees.
Space Complexity: O(1), using only constant extra space.
