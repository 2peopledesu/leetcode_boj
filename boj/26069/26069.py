import sys

input = sys.stdin.readline

n = int(input())

meet = {}

dance_people = set()

for i in range(n):
    a, b = input().split()
    if a == "ChongChong":
        dance_people.add(a)
        dance_people.add(b)
    elif b == "ChongChong":
        dance_people.add(b)
    if a in dance_people or b in dance_people:
        dance_people.add(a)
        dance_people.add(b)

print(len(dance_people))
