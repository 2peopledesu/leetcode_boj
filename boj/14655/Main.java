import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[] firstRound = new int[N];
        int[] secondRound = new int[N];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            firstRound[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < N; i++) {
            secondRound[i] = Integer.parseInt(st.nextToken());
        }

        // 첫 번째 라운드 최대 합 계산
        int maxFirstSum = calculateMaxSum(firstRound, N);
        // 두 번째 라운드 최소 합 계산
        int minSecondSum = calculateMinSum(secondRound, N);

        // 최종 점수 계산
        int score = maxFirstSum - minSecondSum;
        System.out.println(score);
    }

    private static int calculateMaxSum(int[] coins, int N) {
        int[] dp = new int[N + 1];
        for (int i = 0; i < N; i++) {
            dp[i + 1] = dp[i] + Math.max(coins[i], -coins[i]); // 최대값 선택
            if (i >= 2) {
                dp[i + 1] = Math.max(dp[i + 1], dp[i - 1] + Math.max(coins[i], -coins[i])); // 3개 연속 뒤집기
            }
        }
        return dp[N];
    }

    private static int calculateMinSum(int[] coins, int N) {
        int[] dp = new int[N + 1];
        for (int i = 0; i < N; i++) {
            dp[i + 1] = dp[i] + Math.min(coins[i], -coins[i]); // 최소값 선택
            if (i >= 2) {
                dp[i + 1] = Math.min(dp[i + 1], dp[i - 1] + Math.min(coins[i], -coins[i])); // 3개 연속 뒤집기
            }
        }
        return dp[N];
    }
}