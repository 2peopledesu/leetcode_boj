import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] a = new int[n];
        int[] b = new int[m]; 

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        StringBuilder sb = new StringBuilder();
        int i = 0, j = 0;
        while (i < n && j < m) {
            if (a[i] < b[j]) {
                sb.append(a[i]).append(" ");
                i++;
            } else {
                sb.append(b[j]).append(" ");
                j++;
            }
        }

        while (i < n) {
            sb.append(a[i++]).append(" ");
        }
        
        while (j < m) {
            sb.append(b[j++]).append(" ");
        }
        System.out.println(sb.toString());
    }
}
