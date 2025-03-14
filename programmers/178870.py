def solution(sequence, k):
    n = len(sequence)
    left = 0
    current_sum = 0
    answer = [0, n-1]
    
    for right in range(n):
        current_sum += sequence[right]
        
        while current_sum > k and left <= right:
            current_sum -= sequence[left]
            left += 1
        
        if current_sum == k:
            if right - left < answer[1] - answer[0]:
                answer = [left, right]
    
    return answer