from collections import Counter

def solution(weights):
    answer = 0
    weight_count = Counter(weights)
    
    for weight, count in weight_count.items():
        if count > 1:
            answer += (count * (count - 1)) // 2
    
    for weight in sorted(weight_count.keys()):
        w = weight_count[weight]
        
        if (weight * 3) % 2 == 0 and (weight * 3) // 2 in weight_count:
            answer += w * weight_count[(weight * 3) // 2]
            
        if weight * 2 in weight_count:
            answer += w * weight_count[weight * 2]
            
        if (weight * 4) % 3 == 0 and (weight * 4) // 3 in weight_count:
            answer += w * weight_count[(weight * 4) // 3]
    
    return answer