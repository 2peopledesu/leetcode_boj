# 택배 상자 꺼내기

def solution(n, w, num):
    height = (n + w - 1) // w
    boxes = list([0] * w for _ in range(height))
            
    count = 1
    now_num = 1
    result = 0
    
    target_i, target_j = 0, 0
    for i in range(height):
        if count % 2 == 1:
            for j in range(w):
                boxes[i][j] = now_num
                if now_num == num:
                    target_i, target_j = i, j
                now_num += 1
        else:
            for j in range(w - 1, -1, -1):
                boxes[i][j] = now_num
                if now_num == num:
                    target_i, target_j = i, j
                now_num += 1
        count += 1
    
    for i in range(w):
        if height * w - i > n:
            if height % 2 == 1:
                boxes[height - 1][w - 1 - i] = -1
            else:
                boxes[height - 1][i] = -1
        
    for i in range(target_i, height):
        if boxes[i][target_j] != -1:
            result += 1
    
    print(boxes)
    
    return result