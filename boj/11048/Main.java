import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n + 1][m + 1];
        int[][] dp = new int[n + 1][m + 1];

        for (int i = 1; i <= n; i ++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 1; j <= m; j ++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        dp[1][1] = board[1][1];

        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= m; j ++) {
                if(i == 1 && j == 1) {
                    continue;
                }
                dp[i][j] = Math.max(Math.max(dp[i - 1][j], dp[i][j - 1]), dp[i - 1][j - 1]) + board[i][j];
            }
        }

        System.out.println(dp[n][m]);
    }
}

