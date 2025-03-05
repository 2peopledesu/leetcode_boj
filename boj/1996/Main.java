import java.io.*;

public class Main {
    public static int[] dx = { 0, 0, 1, -1, 1, 1, -1, -1 };
    public static int[] dy = { 1, -1, 0, 0, 1, -1, 1, -1 };

    public static boolean isArray(int x, int y, int N) {
        return x >= 0 && x < N && y >= 0 && y < N;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());
        int[][] board = new int[N][N];
        int[][] result = new int[N][N];

        for (int i = 0; i < N; i++) {
            String line = br.readLine();
            for (int j = 0; j < N; j++) {
                char ch = line.charAt(j);
                if (ch == '.') {
                    board[i][j] = 0;
                } else {
                    board[i][j] = ch - '0';
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] != 0) {
                    for (int k = 0; k < 8; k++) {
                        int nx = i + dx[k];
                        int ny = j + dy[k];
                        if (isArray(nx, ny, N)) {
                            result[nx][ny] += board[i][j];
                        }
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                if (board[i][j] == 0) {
                    if (result[i][j] > 9) {
                        System.out.print('M');
                    } else {
                        System.out.print(result[i][j]);
                    }
                } else {
                    System.out.print('*');
                }
            }
            System.out.println();
        }
    }
}
