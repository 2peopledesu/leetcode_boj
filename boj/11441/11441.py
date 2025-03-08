import sys

input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))

prefix_sum = [0] * (n+1)

for i in range(1, n+1):
    prefix_sum[i] = prefix_sum[i-1] + arr[i-1]

m = int(input())

for i in range(m):
    start, end = map(int, input().split())
    print(prefix_sum[end] - prefix_sum[start-1])