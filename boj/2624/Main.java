import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());
        int k = Integer.parseInt(br.readLine());
        int[] values = new int[k + 1];
        int[] counts = new int[k + 1];
        int[][] dp = new int[t + 1][k + 1];
        
        for (int i = 1; i <= k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            values[i] = Integer.parseInt(st.nextToken());
            counts[i] = Integer.parseInt(st.nextToken());
        }

        for (int i = 1; i <= k; i++) {
            int val = values[i];
            int cnt = counts[i];
            dp[0][i - 1] = 1;

            for (int j = 1; j <= cnt; j++) {
                for (int l = val * j; l <= t; l++) {
                    dp[l][i] += dp[l - (val * j)][i - 1];
                }
            }

            for (int j = 1; j <= t; j++) {
                dp[j][i] += dp[j][i - 1];
            }
        }
        
        System.out.println(dp[t][k]);
    }
}