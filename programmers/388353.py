import heapq

def is_valid(x, y, storage_board):
    return 0 <= x < len(storage_board) and 0 <= y < len(storage_board[0])

def solution(storage, requests):
    original_len = len(storage)
    storage_board = [[0] * (len(storage[0]) + 2)]
    storage_board += [[0] + list(string) +[0] for string in storage]
    storage_board += [[0] * (len(storage[0]) + 2)]
    answer = 0
    
    dx, dy = [-1, 0, 1, 0], [0, 1, 0, -1]
    
    for i in range(len(requests)):
        if len(requests[i]) == 1:
            visited = [[0] * (len(storage[0]) + 2) for _ in range(len(storage) + 2)]
            q = []
            heapq.heappush(q, (0, 0))
            
            while q:
                x, y = heapq.heappop(q)
                for j in range(4):
                    nx, ny = x + dx[j], y + dy[j]
                    if is_valid(nx, ny, storage_board) and not visited[nx][ny]:
                        if storage_board[nx][ny] == 0:
                            visited[nx][ny] = True
                            heapq.heappush(q, (nx, ny))
                        elif storage_board[nx][ny] == requests[i][0]:
                            visited[nx][ny] = True
                            storage_board[nx][ny] = 0
                            
        if len(requests[i]) == 2:
            for k in range(len(storage_board)):
                for l in range(len(storage_board[0])):
                    if storage_board[k][l] == requests[i][0]:
                        storage_board[k][l] = 0
    
    for i in range(len(storage_board)):
        for j in range(len(storage_board[0])):
            if storage_board[i][j] != 0:
                answer += 1
        
    return answer

print(solution(["HAH", "HBH", "HHH", "HAH", "HBH"],["C", "B", "B", "B", "B", "H"]))