import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];

        int resultMax = 1;
        int resultMin = 1;
        int min = 1;
        int max = 1;

        String[] input = br.readLine().split(" ");
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(input[i]);
        }

        for (int i = 0; i < n - 1; i++) {
            if (arr[i] <= arr[i + 1]) {
                min++;
            } else {
                resultMin = Math.max(min, resultMin);
                min = 1;
            }
            if (arr[i] >= arr[i + 1]) {
                max++;
            } else {
                resultMax = Math.max(max, resultMax);
                max = 1; 
            }
        }
        
        resultMin = Math.max(min, resultMin);
        resultMax = Math.max(max, resultMax);
        
        System.out.println(Math.max(resultMax, resultMin));
    }
}