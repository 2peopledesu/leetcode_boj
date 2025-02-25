# 17266 어두운 굴다리

## Problem Link

https://www.acmicpc.net/problem/17266

## Solution

This problem finds the minimum height of street lamps needed to illuminate an entire bridge path.

Key Logic:

1. Edge Cases Check:

   - Distance from start (0) to first lamp
   - Distance from last lamp to end (n)
   - These distances need to be fully covered

2. Gap Analysis:

   - Check distances between consecutive lamps
   - For each gap between lamps:
     - Need height to cover half the distance
     - Use (distance + 1) // 2 for ceiling division
     - This ensures complete coverage of gap

3. Maximum Height:
   - Take maximum of:
     - Distance to first lamp
     - Distance from last lamp
     - Half of maximum gap between lamps
   - This gives minimum height needed for full coverage

Time Complexity: O(M), where M is the number of street lamps.
Space Complexity: O(1), using only constant extra space.
