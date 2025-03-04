import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        String street = br.readLine();

        int[] dp = new int[N];
        Arrays.fill(dp, Integer.MAX_VALUE);
        dp[0] = 0;

        for (int i = 1; i < N; i++) {
            char current = street.charAt(i);
            char target = getPrevious(current);

            for (int j = 0; j < i; j ++) {
                if (street.charAt(j) == target && dp[j] !=  Integer.MAX_VALUE) {
                    dp[i] = Math.min(dp[i], dp[j] + (i - j) * (i - j));
                }
            }
        }

        System.out.println(dp[N - 1] == Integer.MAX_VALUE ? -1 : dp[N - 1]);
    }

    static char getPrevious(char current) {
        if (current == 'B') return 'J';
        if (current == 'O') return 'B';
        return 'O';
    }
}
