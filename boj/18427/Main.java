import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int h = Integer.parseInt(st.nextToken());

        List<List<Integer>> blocks = new ArrayList<>();
        blocks.add(new ArrayList<>());
        int[][] dp = new int[n + 1][h + 1];

        dp[0][0] = 1;

        for (int i = 1; i <= n; i++) {
            blocks.add(new ArrayList<>());
            st = new StringTokenizer(br.readLine());
            while(st.hasMoreTokens()){
                int block = Integer.parseInt(st.nextToken());
                if(block <= h) blocks.get(i).add(block);
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 0; j <= h; j++) {
                dp[i][j] = dp[i - 1][j] % 10007;
                for (int block : blocks.get(i)) {
                    if (j >= block) {
                        dp[i][j] += dp[i - 1][j - block] % 10007;
                    }
                }
            }
        }
        System.out.println(dp[n][h] % 10007);
    }
}