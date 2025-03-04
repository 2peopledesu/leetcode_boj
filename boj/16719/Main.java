import java.io.*;

public class Main {
    static String str;
    static boolean[] visited;
    static StringBuilder sb = new StringBuilder();
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        str = br.readLine();
        visited = new boolean[str.length()];
        
        solve(0, str.length() - 1);
        System.out.print(sb.toString());
    }
    
    static void solve(int left, int right) {
        if (left > right) return;
        
        int minIndex = left;
        for (int i = left; i <= right; i++) {
            if (!visited[i] && str.charAt(minIndex) > str.charAt(i)) {
                minIndex = i;
            }
        }
        
        visited[minIndex] = true;
        
        printCurrentString();
        
        solve(minIndex + 1, right);
        solve(left, minIndex - 1);
    }
    
    static void printCurrentString() {
        for (int i = 0; i < str.length(); i++) {
            if (visited[i]) {
                sb.append(str.charAt(i));
            }
        }
        sb.append("\n");
    }
}