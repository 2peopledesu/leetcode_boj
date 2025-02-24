import sys

input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
calendar = [[0]*366 for _ in range(1000)]  # 행 최대 1000개, 날짜 1~365일

arr.sort(key=lambda x: (x[0], -x[1]))  # 시작일 오름차순, 종료일 내림차순 정렬

# 1. 일정을 캘린더에 배치
for elem in arr:
    s, e = elem[0], elem[1]
    # 현재 일정을 넣을 수 있는 가장 낮은 행 찾기
    row = 0
    while True:
        if all(calendar[row][day] == 0 for day in range(s, e+1)):
            break
        row += 1
    # 찾은 행에 일정 표시
    for day in range(s, e+1):
        calendar[row][day] = 1

# 2. 연속된 블록 그룹화
groups = []
current_start = -1
current_end = -1
for day in range(1, 366):
    has_schedule = any(calendar[row][day] == 1 for row in range(1000))
    if has_schedule:
        if current_start == -1:
            current_start = day
        current_end = day
    else:
        if current_start != -1:
            groups.append((current_start, current_end))
            current_start = -1
            current_end = -1
if current_start != -1:
    groups.append((current_start, current_end))

# 3. 각 블록의 최대 높이 계산
result = 0
for s, e in groups:
    max_height = 0
    for day in range(s, e+1):
        cnt = sum(calendar[row][day] for row in range(1000))
        max_height = max(max_height, cnt)
    result += (e - s + 1) * max_height

print(result)