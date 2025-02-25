import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static int[] dx = { 0, 0, 1, -1, 0, 0 };
    public static int[] dy = { 1, -1, 0, 0, 0, 0 };
    public static int[] dz = { 0, 0, 0, 0, 1, -1 };

    public static boolean isValid(int x, int y, int z, int h, int n, int m) {
        return x >= 0 && x < h && y >= 0 && y < n && z >= 0 && z < m;
    }

    public static boolean find_0(int[][][] box, int h, int n, int m) {
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (box[i][j][k] == 0) {
                        return false;
                    }
                }
            }
        }
        return true;
    }

    public static void bfs(int[][][] box, int h, int n, int m) {
        Queue<int[]> queue = new LinkedList<>();
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (box[i][j][k] == 1) {
                        queue.offer(new int[] { i, j, k });
                    }
                }
            }
        }
        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];
            int z = current[2];
            for (int i = 0; i < 6; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                int nz = z + dz[i];
                if (isValid(nx, ny, nz, h, n, m) && box[nx][ny][nz] == 0) {
                    box[nx][ny][nz] = box[x][y][z] + 1;
                    queue.offer(new int[] { nx, ny, nz });
                }
            }
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int m = scanner.nextInt();
        int n = scanner.nextInt();
        int h = scanner.nextInt();
        int[][][] box = new int[h][n][m];
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    box[i][j][k] = scanner.nextInt();
                }
            }
        }
        if (find_0(box, h, n, m)) {
            System.out.println(0);
            return;
        }
        bfs(box, h, n, m);
        int max = 0;
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    if (box[i][j][k] == 0) {
                        System.out.println(-1);
                        return;
                    }
                    max = Math.max(max, box[i][j][k]);
                }
            }
        }
        System.out.println(max - 1);
    }
}
