import java.io.*;

public class Main {
    static int N;
    static char[][] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        N = Integer.parseInt(br.readLine());
        arr = new char[N][N];

        for (int i = 0; i < N; i++) {
            String s = br.readLine();
            arr[i] = s.toCharArray(); // char 배열로 변환
        }
        
        int result = 0;

        for (int r = 0; r < N; r++) {
            for (int c = 0; c < N; c++) {
                result = Math.max(result, getMax(r, c)); // 교환 전에 최대 개수 체크
                if (r + 1 < N) {
                    swap(r, c, r + 1, c);
                    result = Math.max(result, Math.max(getMax(r, c), getMax(r + 1, c)));
                    swap(r, c, r + 1, c);
                }
                if (c + 1 < N) {
                    swap(r, c, r, c + 1);
                    result = Math.max(result, Math.max(getMax(r, c), getMax(r, c + 1)));
                    swap(r, c, r, c + 1);
                }
            }
        }
        
        bw.write(String.valueOf(result)); // 결과 출력
        bw.newLine(); // 줄바꿈
        bw.flush(); // 버퍼 비우기
        bw.close(); // BufferedWriter 닫기
        br.close(); // BufferedReader 닫기
    }

    static int getMax(int r, int c) {
        char ch = arr[r][c];
        int rCnt = 0;
        int cCnt = 0;

        // 상 하 체크
        int nr = r + 1; // 하
        int nc = c;

        while (nr < N && arr[nr++][nc] == ch) {
            rCnt++;
        }
        nr = r - 1; // 상
        while (nr >= 0 && arr[nr--][nc] == ch) {
            rCnt++;
        }

        // 좌 우 체크
        nr = r; // 우
        nc = c + 1;
        while (nc < N && arr[nr][nc++] == ch) cCnt++;
        nc = c - 1; // 좌
        while (nc >= 0 && arr[nr][nc--] == ch) cCnt++;

        return Math.max(rCnt, cCnt) + 1;
    }

    static void swap(int r, int c, int i, int j) {
        char tmp = arr[r][c];
        arr[r][c] = arr[i][j];
        arr[i][j] = tmp;
    }
}
