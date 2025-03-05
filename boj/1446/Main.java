import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int D = Integer.parseInt(st.nextToken());
        int[] dp = new int[D + 1];

        for(int i = 0; i <= D; i++){
            dp[i] = i;
        }

        int[][] shortPath = new int[N][3];

        for(int i = 0; i < N; i++){
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            int distance = Integer.parseInt(st.nextToken());

            shortPath[i][0] = start;
            shortPath[i][1] = end;
            shortPath[i][2] = distance;
        }

        Arrays.sort(shortPath, (a, b) -> a[0] - b[0]);

        for(int i = 0; i < N; i++){
            int start = shortPath[i][0];
            int end = shortPath[i][1];
            int distance = shortPath[i][2];

            if(end > D) continue;

            for (int j = 1; j < D + 1; j ++) {
                if(end == j) {
                    dp[j] = Math.min(dp[j], dp[start] + distance);
                } else {
                    dp[j] = Math.min(dp[j], dp[j - 1] + 1);
                }
            }
        }

        System.out.println(dp[D]);
    }
}