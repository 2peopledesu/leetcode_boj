from collections import Counter

def solution(points, routes):
    def calculate_path(route):
        paths = []
        time = 0
        
        for i in range(len(route) - 1):
            sx, sy = points[route[i] - 1]
            ex, ey = points[route[i + 1] - 1]
            
            # 시작 위치 저장 (첫 지점이거나 이전 위치와 다른 경우만)
            if not paths or (paths[-1][0], paths[-1][1]) != (sx, sy):
                paths.append((sx, sy, time))
                time += 1
            
            # x 좌표 맞추기
            while sx != ex:
                if sx < ex:
                    sx += 1
                else:
                    sx -= 1
                paths.append((sx, sy, time))
                time += 1
            
            # y 좌표 맞추기
            while sy != ey:
                if sy < ey:
                    sy += 1
                else:
                    sy -= 1
                paths.append((sx, sy, time))
                time += 1
        
        # 마지막 위치가 추가되지 않았다면 추가
        last_point = route[-1]
        last_x, last_y = points[last_point - 1]
        if not paths or (paths[-1][0], paths[-1][1]) != (last_x, last_y):
            paths.append((last_x, last_y, time))
            
        return paths
    
    all_paths = []
    for route in routes:
        all_paths.extend(calculate_path(route))
    
    # 경로 카운팅 (x, y, time)이 같은 경우 = 충돌
    path_counter = Counter(all_paths)
    
    collisions = sum(1 for count in path_counter.values() if count >= 2)
    
    return collisions