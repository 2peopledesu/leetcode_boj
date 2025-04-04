# README.md

## 문제 설명

이 문제는 주어진 도로의 길이 \( D \)와 \( N \)개의 단축키를 이용하여 최단 경로를 찾는 문제입니다. 각 단축키는 시작점, 도착점, 그리고 해당 경로의 길이를 제공합니다. 목표는 도착점까지의 최단 거리를 계산하는 것입니다.

## DP로 문제를 푸는 이유

1. **최적 부분 구조**: 문제는 최단 경로를 찾는 문제로, 최단 경로를 구성하는 부분 경로의 최단 거리도 최단 경로의 일부입니다. 즉, 특정 지점까지의 최단 거리를 알고 있다면, 그 지점을 포함한 경로의 최단 거리도 쉽게 계산할 수 있습니다.

2. **중복 부분 문제**: 여러 경로에서 동일한 지점에 도달할 수 있으며, 이 경우 동일한 계산을 반복하게 됩니다. DP를 사용하면 이미 계산된 값을 저장하여 중복 계산을 피할 수 있습니다.

3. **상태 전이**: 각 지점까지의 최단 거리를 `dp` 배열에 저장하고, 단축키를 통해 해당 지점까지의 거리를 업데이트하는 방식으로 문제를 해결합니다. 이는 DP의 전형적인 접근 방식입니다.

## 시간 복잡도

- **입력 처리**: \( O(N) \) - \( N \)개의 단축키를 입력받습니다.
- **정렬**: \( O(N \log N) \) - 단축키를 시작점 기준으로 정렬합니다.
- **DP 업데이트**: \( O(N \cdot D) \) - 각 단축키에 대해 최대 \( D \)까지의 거리 업데이트를 수행합니다.

따라서 전체 시간 복잡도는 \( O(N \log N + N \cdot D) \)입니다.

## 공간 복잡도

- **DP 배열**: \( O(D) \) - 최단 거리를 저장하기 위한 배열입니다.
- **단축키 배열**: \( O(N) \) - 입력받은 단축키를 저장하기 위한 배열입니다.

따라서 전체 공간 복잡도는 \( O(N + D) \)입니다. 이 또한 효율적인 공간 사용입니다.

## 결론

이 문제는 DP를 통해 최단 경로를 효율적으로 계산할 수 있으며, 시간 복잡도와 공간 복잡도 모두 합격 기준을 만족합니다.
