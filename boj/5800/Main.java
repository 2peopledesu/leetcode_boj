import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int K = Integer.parseInt(br.readLine());
        
        for (int i = 1; i <= K; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int N = Integer.parseInt(st.nextToken());
            
            int[] scores = new int[N];
            for (int j = 0; j < N; j++) {
                scores[j] = Integer.parseInt(st.nextToken());
            }
            
            Arrays.sort(scores);
            
            int maxGap = 0;
            for (int j = 1; j < N; j++) {
                maxGap = Math.max(maxGap, scores[j] - scores[j-1]);
            }
            
            sb.append("Class ").append(i).append('\n');
            sb.append("Max ").append(scores[N-1])
              .append(", Min ").append(scores[0])
              .append(", Largest gap ").append(maxGap).append('\n');
        }
        
        System.out.print(sb);
    }
}
