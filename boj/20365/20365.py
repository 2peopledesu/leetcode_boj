import sys

input = sys.stdin.readline

n = int(input())
s = input()

BL= 0
RE = 0

previous_color = ""

if s[0] == "B":
    BL += 1
    previous_color = "B"
else:
    RE += 1
    previous_color = "R"

for i in range(1, n):
    if s[i] != previous_color:
        if s[i] == "B":
            BL += 1
            previous_color = "B"
        else:
            RE += 1
            previous_color = "R"
            
print(min(BL, RE) + 1)