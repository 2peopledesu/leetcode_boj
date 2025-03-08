import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int M = Integer.parseInt(st.nextToken());
        int N = Integer.parseInt(st.nextToken());
        int[] ans = new int[5];
        int[] blind = new int[N];
        br.readLine();

        for (int i = 0; i < M; i++) {
            for (int j = 0; j < 4; j++) {
                String line = br.readLine();
                for (int k = 0; k < N; k++) {
                    if (line.charAt(5 * k + 1) == '*') {
                        blind[k]++;
                    }
                }
            }
            for (int k = 0; k < N; k++) {
                ans[blind[k]]++;
            }
            Arrays.fill(blind, 0);
            br.readLine();
        }

        for (int i = 0; i < 5; i++) {
            if (i == 4) {
                System.out.println(ans[i]);
            } else {
                System.out.print(ans[i] + " ");
            }
        }
    }
}