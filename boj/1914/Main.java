import java.io.*;
import java.math.BigInteger;

public class Main {
    static StringBuilder sb = new StringBuilder();
    static int count = 0;
    
    public static void moveHanoi(int n, int from, int to, int aux) {
        if (n == 1) {
            sb.append(from).append(" ").append(to).append("\n");
            return;
        }
        
        moveHanoi(n-1, from, aux, to);
        sb.append(from).append(" ").append(to).append("\n");
        
        moveHanoi(n-1, aux, to, from);
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        
        BigInteger count = new BigInteger("2").pow(N).subtract(BigInteger.ONE);
        System.out.println(count);
        
        if (N <= 20) {
            moveHanoi(N, 1, 3, 2);
            System.out.print(sb.toString());
        }
    }
}