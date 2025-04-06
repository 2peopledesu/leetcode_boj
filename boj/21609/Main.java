import java.io.*;
import java.util.*;

public class Main {
    static int n, m;
    static int[] dx = {-1, 0, 0, 1};
    static int[] dy = {0, -1, 1, 0};
    static int[][] map;
    static boolean[][] visited;
    static int totalScore = 0;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][n];
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        while (true) {
            List<int[]> biggestGroup = findBiggestGroup();
            if (biggestGroup.size() < 2) break;
            
            int score = removeBlocks(biggestGroup);
            totalScore += score;
            
            applyGravity();
            
            rotateCounterClockwise();
            
            applyGravity();
        }
        
        System.out.println(totalScore);
    }

    static List<int[]> findBiggestGroup() {
        visited = new boolean[n][n];
        List<int[]> maxGroup = new ArrayList<>();
        int maxSize = 0;
        int maxRainbow = 0;
        int maxRow = -1;
        int maxCol = -1;
        
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (map[i][j] > 0 && !visited[i][j]) {
                    List<int[]> group = new ArrayList<>();
                    List<int[]> rainbows = new ArrayList<>();
                    int baseColor = map[i][j];
                    
                    Queue<int[]> queue = new LinkedList<>();
                    queue.add(new int[]{i, j});
                    group.add(new int[]{i, j});
                    visited[i][j] = true;
                    
                    while (!queue.isEmpty()) {
                        int[] cur = queue.poll();
                        int x = cur[0];
                        int y = cur[1];
                        
                        for (int d = 0; d < 4; d++) {
                            int nx = x + dx[d];
                            int ny = y + dy[d];
                            
                            if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                                if (!visited[nx][ny] && (map[nx][ny] == baseColor || map[nx][ny] == 0)) {
                                    visited[nx][ny] = true;
                                    queue.add(new int[]{nx, ny});
                                    group.add(new int[]{nx, ny});
                                    
                                    if (map[nx][ny] == 0) {
                                        rainbows.add(new int[]{nx, ny});
                                    }
                                }
                            }
                        }
                    }
                    
                    for (int[] rainbow : rainbows) {
                        visited[rainbow[0]][rainbow[1]] = false;
                    }
                    
                    int standardRow = n;
                    int standardCol = n;
                    for (int[] block : group) {
                        if (map[block[0]][block[1]] > 0) {
                            if (block[0] < standardRow || (block[0] == standardRow && block[1] < standardCol)) {
                                standardRow = block[0];
                                standardCol = block[1];
                            }
                        }
                    }
                    
                    if (group.size() > maxSize || 
                        (group.size() == maxSize && rainbows.size() > maxRainbow) ||
                        (group.size() == maxSize && rainbows.size() == maxRainbow && standardRow > maxRow) ||
                        (group.size() == maxSize && rainbows.size() == maxRainbow && standardRow == maxRow && standardCol > maxCol)) {
                        maxSize = group.size();
                        maxRainbow = rainbows.size();
                        maxRow = standardRow;
                        maxCol = standardCol;
                        maxGroup = new ArrayList<>(group);
                    }
                }
            }
        }
        
        return maxGroup;
    }
    
    static int removeBlocks(List<int[]> group) {
        for (int[] block : group) {
            map[block[0]][block[1]] = -2;
        }
        return group.size() * group.size();
    }
    
    static void applyGravity() {
        for (int j = 0; j < n; j++) {
            for (int i = n - 2; i >= 0; i--) {
                if (map[i][j] >= 0) {
                    int row = i;
                    while (row + 1 < n && map[row + 1][j] == -2) {
                        map[row + 1][j] = map[row][j];
                        map[row][j] = -2;
                        row++;
                    }
                }
            }
        }
    }
    
    static void rotateCounterClockwise() {
        int[][] newMap = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                newMap[n - 1 - j][i] = map[i][j];
            }
        }
        map = newMap;
    }
}