import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        
        StringBuilder sb = new StringBuilder();
        for (int t = 0; t < T; t++) {
            int N = Integer.parseInt(br.readLine().trim());
            int[] cards = new int[N];
            
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int i = 0; i < N; i++) {
                cards[i] = Integer.parseInt(st.nextToken());
            }
            
            sb.append(getGeunwooScore(cards, N)).append("\n");
        }
        
        System.out.print(sb);
    }
    
    private static int getGeunwooScore(int[] cards, int N) {
        // dp[i][j] = i부터 j까지의 카드가 남았을 때 얻을 수 있는 최대 점수 차이
        int[][] dp = new int[N][N];
        
        // 기저 사례: 카드가 하나일 때
        for (int i = 0; i < N; i++) {
            dp[i][i] = cards[i];
        }
        
        // 길이가 2인 구간부터 차례로 계산
        for (int len = 2; len <= N; len++) {
            for (int i = 0; i <= N - len; i++) {
                int j = i + len - 1;
                // 왼쪽 카드를 선택하는 경우와 오른쪽 카드를 선택하는 경우 중 최대값
                dp[i][j] = Math.max(cards[i] - dp[i+1][j], cards[j] - dp[i][j-1]);
            }
        }
        
        // 총 점수 계산
        int totalSum = 0;
        for (int card : cards) {
            totalSum += card;
        }
        
        // 근우의 점수 = (전체 합 + 점수 차이) / 2
        return (totalSum + dp[0][N-1]) / 2;
    }
}