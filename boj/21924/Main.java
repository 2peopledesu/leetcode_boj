import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        boolean[] visited = new boolean[N + 1];

        HashMap<Integer, ArrayList<int[]>> graph = new HashMap<>();
        long totalCost = 0;

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            graph.computeIfAbsent(a, k -> new ArrayList<>()).add(new int[] { b, c });
            graph.computeIfAbsent(b, k -> new ArrayList<>()).add(new int[] { a, c });
            totalCost += c;
        }

        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[1] - b[1]);
        pq.offer(new int[] { 1, 0 });

        long result = 0;
        int count = 0;

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int node = current[0];
            int cost = current[1];

            if (visited[node]) continue;
            visited[node] = true;
            result += cost;
            count++;

            for (int[] next : graph.get(node)) {
                if (!visited[next[0]]) pq.offer(next);
            }
        }

        if (count != N) {
            System.out.println(-1);
        } else {
            System.out.println(totalCost - result);
        }
    }
}
