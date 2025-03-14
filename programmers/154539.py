def solution(numbers):
    n = len(numbers)
    answer = [-1] * n
    stack = []
    
    for i in range(n):
        while stack and numbers[stack[-1]] < numbers[i]:
            j = stack.pop()
            answer[j] = numbers[i]
        
        stack.append(i)
    
    return answer