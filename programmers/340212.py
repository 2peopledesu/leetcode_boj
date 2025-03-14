def calculate_total_time(diffs, times, level):
    total_time = 0
    
    for i in range(len(diffs)):
        if diffs[i] <= level:
            total_time += times[i]
        else:
            mistakes = diffs[i] - level
            
            if i > 0:
                total_time += mistakes * (times[i] + times[i-1])
            else:
                total_time += mistakes * times[i]
                
            total_time += times[i]
    
    return total_time

def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right
    
    while left <= right:
        mid = (left + right) // 2
        total_time = calculate_total_time(diffs, times, mid)
        
        if total_time <= limit:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    
    return answer

print(solution([1, 5, 3], [2, 4, 7]	, 30))