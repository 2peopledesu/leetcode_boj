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

        int maxFirstSum = calculateMaxSum(firstRound, N);

        int minSecondSum = calculateMinSum(secondRound, N);

        int score = maxFirstSum - minSecondSum;
        System.out.println(score);
    }

    private static int calculateMaxSum(int[] coins, int N) {
        int[] dp = new int[N + 1];
        for (int i = 0; i < N; i++) {
            dp[i + 1] = dp[i] + Math.max(coins[i], -coins[i]);
            if (i >= 2) {
                dp[i + 1] = Math.max(dp[i + 1], dp[i - 1] + Math.max(coins[i], -coins[i]));
            }
        }
        return dp[N];
    }

    private static int calculateMinSum(int[] coins, int N) {
        int[] dp = new int[N + 1];
        for (int i = 0; i < N; i++) {
            dp[i + 1] = dp[i] + Math.min(coins[i], -coins[i]);
            if (i >= 2) {
                dp[i + 1] = Math.min(dp[i + 1], dp[i - 1] + Math.min(coins[i], -coins[i]));
            }
        }
        return dp[N];
    }
}