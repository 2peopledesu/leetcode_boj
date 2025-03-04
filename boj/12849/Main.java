import java.io.*;

public class Main {
    static final int MOD = 1_000_000_007;
    static final int INFO = 0;  // 정보과학관
    static final int COMP = 1;  // 전산관
    static final int FUTURE = 2;  // 미래관 
    static final int SHIN = 3;  // 신양관
    static final int KYUNG = 4;  // 한경직기념관
    static final int TRUTH = 5;  // 진리관
    static final int STUDENT = 6;  // 학생회관
    static final int HYUNG = 7;  // 형남공학관
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int D = Integer.parseInt(br.readLine());
        
        long[][] dp = new long[D + 1][8];
        
        dp[0][INFO] = 1;
        
        for (int t = 1; t <= D; t++) {
            dp[t][INFO] = (dp[t-1][COMP] + dp[t-1][FUTURE]) % MOD;
            
            dp[t][COMP] = (dp[t-1][INFO] + dp[t-1][FUTURE] + dp[t-1][SHIN]) % MOD;
            
            dp[t][FUTURE] = (dp[t-1][INFO] + dp[t-1][COMP] + dp[t-1][SHIN] + dp[t-1][KYUNG]) % MOD;
            
            dp[t][SHIN] = (dp[t-1][COMP] + dp[t-1][FUTURE] + dp[t-1][KYUNG] + dp[t-1][TRUTH]) % MOD;
            
            dp[t][KYUNG] = (dp[t-1][FUTURE] + dp[t-1][SHIN] + dp[t-1][TRUTH] + dp[t-1][HYUNG]) % MOD;
            
            dp[t][TRUTH] = (dp[t-1][SHIN] + dp[t-1][KYUNG] + dp[t-1][STUDENT]) % MOD;
            
            dp[t][STUDENT] = (dp[t-1][TRUTH] + dp[t-1][HYUNG]) % MOD;
            
            dp[t][HYUNG] = (dp[t-1][KYUNG] + dp[t-1][STUDENT]) % MOD;
        }
        
        System.out.println(dp[D][INFO]);
    }
}