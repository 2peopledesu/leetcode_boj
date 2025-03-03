import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        
        for (int tc = 0; tc < t; tc++) {
            int n = Integer.parseInt(br.readLine());
            
            int[][] locations = new int[n + 2][2];
            
            String[] home = br.readLine().split(" ");
            locations[0][0] = Integer.parseInt(home[0]);
            locations[0][1] = Integer.parseInt(home[1]);
            
            for (int i = 1; i <= n; i++) {
                String[] store = br.readLine().split(" ");
                locations[i][0] = Integer.parseInt(store[0]);
                locations[i][1] = Integer.parseInt(store[1]);
            }
            
            String[] festival = br.readLine().split(" ");
            locations[n + 1][0] = Integer.parseInt(festival[0]);
            locations[n + 1][1] = Integer.parseInt(festival[1]);
            
            boolean result = canReachFestival(locations, n);
            
            if (result) {
                System.out.println("happy");
            } else {
                System.out.println("sad");
            }
        }
    }
    
    public static int getDistance(int[] a, int[] b) {
        return Math.abs(a[0] - b[0]) + Math.abs(a[1] - b[1]);
    }
    
    public static boolean canReachFestival(int[][] locations, int n) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[n + 2];
        
        queue.offer(0);
        visited[0] = true;
        
        while (!queue.isEmpty()) {
            int current = queue.poll();
            
            if (current == n + 1) {
                return true;
            }
            
            for (int i = 0; i < n + 2; i++) {
                if (!visited[i]) {
                    if (getDistance(locations[current], locations[i]) <= 1000) {
                        queue.offer(i);
                        visited[i] = true;
                    }
                }
            }
        }
        
        return false;
    }
}