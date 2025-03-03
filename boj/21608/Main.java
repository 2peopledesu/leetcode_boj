import java.io.*;
import java.util.*;

public class Main {
    public static int[] dx = {-1, 1, 0, 0};
    public static int[] dy = {0, 0, -1, 1};

    public static boolean isArray(int x, int y, int n) {
        return x >= 0 && x < n && y >= 0 && y < n;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine().trim());
        int[][] board = new int[n][n];
        
        // 각 학생별 좋아하는 학생 정보를 저장
        HashMap<Integer, int[]> preference = new HashMap<>();
        int[] order = new int[n*n]; // 학생 배치 순서 저장
        
        for (int i = 0; i < (n*n); i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int studentNum = Integer.parseInt(st.nextToken());
            order[i] = studentNum;
            
            int[] likes = new int[4];
            for (int j = 0; j < 4; j++) {
                likes[j] = Integer.parseInt(st.nextToken());
            }
            preference.put(studentNum, likes);
        }

        // 학생 배치
        for (int student : order) {
            int[] likes = preference.get(student);
            
            int maxLike = -1;
            int maxEmpty = -1;
            int minRow = n;
            int minCol = n;
            
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (board[i][j] == 0) {
                        int likeCount = 0;
                        int emptyCount = 0;
                        
                        for (int k = 0; k < 4; k++) {
                            int nx = i + dx[k];
                            int ny = j + dy[k];
                            if (isArray(nx, ny, n)) {
                                if (board[nx][ny] == 0) {
                                    emptyCount++;
                                } else {
                                    for (int like : likes) {
                                        if (board[nx][ny] == like) {
                                            likeCount++;
                                            break;
                                        }
                                    }
                                }
                            }
                        }
                        
                        // 조건에 따라 최적 위치 갱신
                        if (likeCount > maxLike || 
                            (likeCount == maxLike && emptyCount > maxEmpty) ||
                            (likeCount == maxLike && emptyCount == maxEmpty && i < minRow) ||
                            (likeCount == maxLike && emptyCount == maxEmpty && i == minRow && j < minCol)) {
                            maxLike = likeCount;
                            maxEmpty = emptyCount;
                            minRow = i;
                            minCol = j;
                        }
                    }
                }
            }
            
            board[minRow][minCol] = student;
        }
        
        // 만족도 계산
        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int student = board[i][j];
                int[] likes = preference.get(student);
                int likeCount = 0;
                
                for (int k = 0; k < 4; k++) {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (isArray(nx, ny, n)) {
                        for (int like : likes) {
                            if (board[nx][ny] == like) {
                                likeCount++;
                                break;
                            }
                        }
                    }
                }
                
                if (likeCount > 0) {
                    result += Math.pow(10, likeCount - 1);
                }
            }
        }
        
        System.out.println(result);
    }
}