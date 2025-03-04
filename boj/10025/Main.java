import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int K = Integer.parseInt(st.nextToken());

        int[] ice = new int[1000001];

        for (int i = 0; i < N; i ++) {
            st = new StringTokenizer(br.readLine());
            int g = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());
            ice[x] = g;
        }

        int sum = 0;
        int windowSize = 2 * K + 1;
        for (int i = 0; i < windowSize && i < ice.length; i ++) {
            sum += ice[i];
        }

        int max = sum;
        
        int left = 0;
        int right = windowSize - 1;

        while(right < ice.length - 1) {
            sum = sum - ice[left] + ice[right + 1];
            max = Math.max(max, sum);
            left ++;
            right ++;
        }
        System.out.println(max);
    }
}