import java.io.*;
import java.util.*;

public class Main {
    static int[] visited;
    static ArrayList<ArrayList<Integer>> graph;
    static int order;

    public static void dfs(int node) {
        visited[node] = ++order;
        
        for (int next : graph.get(node)) {
            if (visited[next] == 0) {
                dfs(next);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        
        visited = new int[n + 1];
        order = 0;
        
        graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }
        
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        
        for (int i = 1; i <= n; i++) {
            Collections.sort(graph.get(i), Collections.reverseOrder());
        }
        
        dfs(r);
        
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(visited[i]).append('\n');
        }
        System.out.print(sb);
    }
}