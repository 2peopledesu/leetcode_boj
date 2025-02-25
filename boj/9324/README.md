# 9324 진짜 메시지

## Problem Link

https://www.acmicpc.net/problem/9324

## Solution

This problem verifies if a message follows a specific encryption rule where every third occurrence of a character must be followed by the same character.

Key Logic:

1. Character Counting:

   - Maintains count array for 26 uppercase letters
   - Tracks frequency of each character
   - Resets count when verification is complete

2. Verification Process:

   - When character count reaches 3:
     - Next character must be same as current
     - If not, message is fake
     - If at string end, message is fake
   - After verification:
     - Reset count for that character
     - Skip next character (using jump flag)

3. Message Validation:
   - Returns "OK" if all rules are followed
   - Returns "FAKE" if any rule is violated
