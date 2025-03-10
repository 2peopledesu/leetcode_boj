def solution(info, n, m):
    max_a = n - 1
    max_b = m - 1 
    
    dp = [[False] * (max_b + 1) for _ in range(max_a + 1)]
    dp[0][0] = True
    
    for a_inc, b_inc in info:
        new_dp = [[False] * (max_b + 1) for _ in range(max_a + 1)]
        for curr_a in range(max_a + 1):
            for curr_b in range(max_b + 1):
                if not dp[curr_a][curr_b]:
                    continue
                new_a = curr_a + a_inc
                new_b = curr_b
                if new_a <= max_a and new_b <= max_b:
                    new_dp[new_a][new_b] = True
                new_a2 = curr_a
                new_b2 = curr_b + b_inc
                if new_a2 <= max_a and new_b2 <= max_b:
                    new_dp[new_a2][new_b2] = True
        dp = new_dp
        
    for a in range(max_a + 1):
        for b in range(max_b + 1):
            if dp[a][b]:
                return a
    return -1