import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        char[][] map = new char[12][6];
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        for (int i = 0; i < 12; i++) {
            String line = br.readLine();
            for (int j = 0; j < 6; j++) {
                map[i][j] = line.charAt(j);
            }
        }

        int count = 0;

        while(true) {
            boolean[][] visited = new boolean[12][6];
            boolean found = false;

            for (int i = 0; i < 12; i++) {
                for (int j = 0; j < 6; j++) {
                    if (map[i][j] != '.' && !visited[i][j]) {
                        char color = map[i][j];
                        List<int[]> toRemove = new ArrayList<>();
                        Queue<int[]> queue = new LinkedList<>();
                        queue.add(new int[]{i, j});
                        visited[i][j] = true;
                        toRemove.add(new int[]{i, j});

                        while (!queue.isEmpty()) {
                            int[] pos = queue.poll();
                            int x = pos[0];
                            int y = pos[1];

                            for (int d = 0; d < 4; d++) {
                                int nx = x + dx[d];
                                int ny = y + dy[d];

                                if (nx >= 0 && nx < 12 && ny >= 0 && ny < 6 && !visited[nx][ny] && map[nx][ny] == color) {
                                    visited[nx][ny] = true;
                                    queue.add(new int[]{nx, ny});
                                    toRemove.add(new int[]{nx, ny});
                                }
                            }
                        }

                        if (toRemove.size() >= 4) {
                            found = true;
                            for (int[] pos : toRemove) {
                                map[pos[0]][pos[1]] = '.';
                            }
                        }
                    }
                }
            }

            if (!found) break;

            // Gravity
            for (int j = 0; j < 6; j++) {
                for (int i = 11; i >= 0; i--) {
                    if (map[i][j] != '.') {
                        int k = i;
                        while (k < 11 && map[k + 1][j] == '.') {
                            map[k + 1][j] = map[k][j];
                            map[k][j] = '.';
                            k++;
                        }
                    }
                }
            }

            count++;
        }

        System.out.println(count);
    }
}