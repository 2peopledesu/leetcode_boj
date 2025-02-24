# 20207 달력

## Problem Link

https://www.acmicpc.net/problem/20207

## Solution

This solution implements a calendar scheduling system using a 2D array approach.

1. Calendar Setup and Schedule Placement:

   - Creates a 2D array representing the calendar (1000 rows × 366 days)
   - Sorts schedules by start date (ascending) and end date (descending)
   - Places each schedule in the lowest possible row where there's no conflict

2. Block Grouping:

   - Groups consecutive days with schedules into blocks
   - Tracks the start and end of each continuous schedule block
   - Handles edge cases like schedules extending to the last day

3. Area Calculation:
   - For each block, calculates:
     - Width = end date - start date + 1
     - Height = maximum number of overlapping schedules
   - Multiplies width × height for each block
   - Sums all block areas for final result
