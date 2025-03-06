import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        int[][] indexedArr = new int[n][2];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            indexedArr[i][0] = arr[i];
            indexedArr[i][1] = i;
        }

        Arrays.sort(indexedArr, Comparator.comparingInt(a -> a[0]));

        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[indexedArr[i][1]] = i;
        }
        
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append(result[i]).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}