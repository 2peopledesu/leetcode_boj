import sys

input = sys.stdin.readline

def min_dice_sum(N, faces):
    if N == 1:
        # N이 1일 경우, 모든 면이 보이기 때문에 5개의 면의 합
        return sum(faces) - max(faces)
    min_face = []
    min_face.append(min(faces[0], faces[5]))
    min_face.append(min(faces[1], faces[4]))
    min_face.append(min(faces[2], faces[3]))
    min_face.sort()
    
    face1 = 4 * (N-1) * (N-2) + (N-2) * (N-2)
    face2 = 4 * (N-1) + 4 * (N-2)
    face3 = 4
    
    result = face1 * min_face[0] + face2 * (min_face[0] + min_face[1]) + face3 * sum(min_face)
    
    return result
    

n = int(input())

arr = list(map(int, input().split()))

result = min_dice_sum(n, arr)
print(result)