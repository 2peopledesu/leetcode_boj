import java.io.*;
import java.util.*;

public class Main {
    static boolean[] visited;
    static List<List<Integer>> synapse;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        synapse = new ArrayList<>();


        for (int i = 0; i <= n; i++) {
            synapse.add(new ArrayList<>());
        }
        
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            synapse.get(u).add(v);
            synapse.get(v).add(u);
        }

        int component = 0;
        int count = 0;

        visited = new boolean[n + 1];

        for (int i = 1; i <= n; i++) {
            if (!visited[i]) {
                int[] result = bfs(i);
                component++;
                count += result[1] - result[0] + 1;
            }
        }
        System.out.println(count + component - 1);
    }

    public static int[] bfs(int start) {
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        visited[start] = true;

        int countEdge = 0;
        int countNode = 0;

        while (!queue.isEmpty()) {
            int node = queue.poll();
            countNode++;
            for (int next : synapse.get(node)) {
                countEdge++;
                if (!visited[next]) {
                    queue.add(next);
                    visited[next] = true;
                }
            }
        }
        return new int[] {countNode, countEdge / 2};
    }
}