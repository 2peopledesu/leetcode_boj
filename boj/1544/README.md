# 1544 사이클 단어

## problem link

https://www.acmicpc.net/problem/1544

## Solution

is_cyclic function: This function checks if two strings are in a rotational relationship by verifying if string a is contained within string b concatenated with itself.

Length-based sorting: The strings are sorted by length to facilitate grouping of strings of the same length.

Grouping process: A new group is initiated based on unvisited strings, and all strings of the same length that are in a rotational relationship are grouped together.
