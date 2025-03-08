import java.io.*;
import java.util.*;

public class Main {
    public static boolean isArray(int x, int y, int n) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] map = new int[n][n];
        boolean[][] visited = new boolean[n][n];

        int[] dx = { 0, 0, 1, -1 };
        int[] dy = { 1, -1, 0, 0 };

        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split("");
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(line[j]);
            }
        }

        int[][] dist = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
        }

        if (map[0][0] == 1) {
            dist[0][0] = 0;
        } else {
            dist[0][0] = 1;
        }

        LinkedList<int[]> queue = new LinkedList<>();
        queue.add(new int[] { 0, 0 });

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];

                if (isArray(nx, ny, n) && !visited[nx][ny]) {
                    visited[nx][ny] = true;
                    if (map[nx][ny] == 1) {
                        dist[nx][ny] = dist[x][y];
                        queue.addFirst(new int[] { nx, ny });
                    } else {
                        dist[nx][ny] = dist[x][y] + 1;
                        queue.addLast(new int[] { nx, ny });
                    }
                }
            }
        }

        System.out.println(dist[n - 1][n - 1]);
    }
}
