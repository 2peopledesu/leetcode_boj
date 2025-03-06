import java.io.*;
import java.util.*;

public class Main {
    public static boolean isTree;
    public static LinkedList<Integer>[] graph = new LinkedList[501];
    public static boolean[] visited = new boolean[501];

    public static void dfs(int node, int parent) {
        for (int neighbor : graph[node]) {
            if (visited[neighbor]) {
                if (neighbor != parent) {
                    isTree = false;
                }
            } else {
                visited[neighbor] = true;
                dfs(neighbor, node);
            }
        }
    }

    public static void main(String[] args) throws IOException {
        int caseNumber = 1;
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String line = br.readLine();
            if (line == null || line.isEmpty()) break;
            StringTokenizer st = new StringTokenizer(line);
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            if (n == 0 && m == 0) break;

            for (int i = 1; i <= n; i++) {
                graph[i] = new LinkedList<>();
            }

            for (int i = 0; i < m; i++) {
                st = new StringTokenizer(br.readLine());
                int a = Integer.parseInt(st.nextToken());
                int b = Integer.parseInt(st.nextToken());
                graph[a].add(b);
                graph[b].add(a);
            }

            Arrays.fill(visited, false);

            int components = 0;
            for (int i = 1; i <= n; i++) {
                if (!visited[i]) {
                    visited[i] = true;
                    isTree = true;
                    dfs(i, -1);
                    if (isTree) {
                        components++;
                    }
                }
            }

            if (components > 1) {
                System.out.println("Case " + caseNumber + ": A forest of " + components + " trees.");
            } else if (components == 1) {
                System.out.println("Case " + caseNumber + ": There is one tree.");
            } else {
                System.out.println("Case " + caseNumber + ": No trees.");
            }

            caseNumber++;
        }
    }
}

