# 6550 부분문자열

## Problem Link

https://www.acmicpc.net/problem/6550

## Solution

This problem checks if string a is a subsequence of string b. Specifically, it verifies if we can create string a by selecting characters from string b in order.

1. Input Processing:

   - Continuously reads input until EOF
   - Each line contains two strings a and b

2. Subsequence Check:

   - Uses an index (a_index) to track characters of string a in order
   - Iterates through each character of string b to check if it matches current character of a
   - If matched, increments a_index and checks if all characters have been found

3. Output:
   - Prints "Yes" if all characters were found
   - Prints "No" if not all characters could be found

Time Complexity: O(N), where N is the length of string b.
