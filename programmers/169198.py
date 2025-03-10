def solution(m, n, startX, startY, balls):
    answer = []
    
    for ballX, ballY in balls:
        candidates = []
        
        if not (startY == ballY and startX > ballX):
            distance = ((startX + ballX) ** 2 + (startY - ballY) ** 2)
            candidates.append(distance)
        
        if not (startY == ballY and startX < ballX):
            distance = ((2 * m - startX - ballX) ** 2 + (startY - ballY) ** 2)
            candidates.append(distance)
        
        if not (startX == ballX and startY > ballY):
            distance = ((startX - ballX) ** 2 + (startY + ballY) ** 2)
            candidates.append(distance)
        
        if not (startX == ballX and startY < ballY):
            distance = ((startX - ballX) ** 2 + (2 * n - startY - ballY) ** 2)
            candidates.append(distance)
        
        answer.append(min(candidates))
    
    return answer