import sys

input = sys.stdin.readline

target = input().strip()
devil = input().strip()
angel = input().strip()

m = len(target)
n = len(angel)

# dp[type][step][position]
dp = [[[0] * n for _ in range(m)] for _ in range(2)]

# init
for potision in range(n):
    if devil[potision] == target[0]:
        dp[0][0][potision] = 1
    if angel[potision] == target[0]:
        dp[1][0][potision] = 1
        
for step in range(m - 1):
    for type in range(2):
        for position in range(n):
            if dp[type][step][position] == 0:
                continue
            next_type = 1 - type
            
            for next_position in range(position + 1, n):
                if (next_type == 0 and devil[next_position] == target[step + 1]) or \
                    (next_type == 1 and angel[next_position] == target[step + 1]):
                        dp[next_type][step + 1][next_position] += dp[type][step][position]

result = 0

for type in range(2):
    for position in range(n):
        result += dp[type][m - 1][position]

print(result)