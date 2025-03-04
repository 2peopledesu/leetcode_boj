import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(input[j]);
            }
        }

        long[][][] dp = new long[n][n][3];

        dp[0][1][0] = 1;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] == 1) continue;
                
                if (j > 0) {
                    dp[i][j][0] += dp[i][j-1][0];
                    dp[i][j][0] += dp[i][j-1][2];
                }
                
                if (i > 0) {
                    dp[i][j][1] += dp[i-1][j][1];
                    dp[i][j][1] += dp[i-1][j][2];
                }
                
                if (i > 0 && j > 0 && map[i-1][j] != 1 && map[i][j-1] != 1) {
                    dp[i][j][2] += dp[i-1][j-1][0];
                    dp[i][j][2] += dp[i-1][j-1][1];
                    dp[i][j][2] += dp[i-1][j-1][2];
                }
            }
        }

        System.out.println(dp[n-1][n-1][0] + dp[n-1][n-1][1] + dp[n-1][n-1][2]);
    }
}