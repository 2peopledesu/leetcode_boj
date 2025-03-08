import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken()) - 1;
        int b = Integer.parseInt(st.nextToken()) - 1;

        int[] visited = new int[n];
        Arrays.fill(visited, -1);
        Queue<Integer> q = new LinkedList<>();
        q.add(a);
        visited[a] = 0;

        while (!q.isEmpty()) {
            int current = q.poll();
            if (current == b) break;

            int step = arr[current];
            if (step == 0) continue; // 0으로 나눌 수 없음

            // 양방향 점프 (배수만큼)
            for (int dir = -1; dir <= 1; dir += 2) {
                for (int jump = step; ; jump += step) {
                    int next = current + dir * jump;
                    if (next < 0 || next >= n) break;
                    if (visited[next] == -1) {
                        visited[next] = visited[current] + 1;
                        q.add(next);
                    }
                }
            }
        }

        System.out.println(visited[b]);
    }
}