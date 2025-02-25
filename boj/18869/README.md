# 18869 멀티버스 II

## Problem Link

https://www.acmicpc.net/problem/18869

## Solution

This problem solves finding the number of "balanced" universe pairs using coordinate compression and frequency counting.

1. Coordinate Compression:

   - For each universe, create index-value pairs
   - Sort by values to assign compressed coordinates
   - Maintain relative order between elements while reducing value range
   - Restore original order using indices

2. Pattern Matching:

   - Convert each compressed universe into a tuple for hashing
   - Count frequency of each pattern using defaultdict
   - Two universes are balanced if they have the same compressed pattern

3. Pair Counting:
   - For each pattern frequency (n), calculate number of possible pairs
   - Use combination formula: n \* (n-1) / 2
   - Sum all pair counts for final result

Time Complexity: O(M \* N log N), where M is number of universes and N is planets per universe.
