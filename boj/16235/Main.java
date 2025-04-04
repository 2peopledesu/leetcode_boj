import java.io.*;
import java.util.*;

public class Main {
    static int N, M, K;
    static int[][] A, nutrient;
    static Deque<Integer>[][] trees;
    static int[] dx = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int[] dy = {-1, 0, 1, -1, 1, -1, 0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        A = new int[N][N];
        nutrient = new int[N][N];
        trees = new ArrayDeque[N][N];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < N; j++) {
                A[i][j] = Integer.parseInt(st.nextToken());
                nutrient[i][j] = 5;
                trees[i][j] = new ArrayDeque<>();
            }
        }

        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken()) - 1;
            int y = Integer.parseInt(st.nextToken()) - 1;
            int age = Integer.parseInt(st.nextToken());
            trees[x][y].add(age);
        }

        while (K-- > 0) {
            springAndSummer();
            fall();
            winter();
        }

        System.out.println(countTrees());
    }

    static void springAndSummer() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                // 봄과 여름을 동시에 처리
                int deadNutrient = 0;
                int size = trees[i][j].size();
                
                for (int t = 0; t < size; t++) {
                    int age = trees[i][j].pollFirst();
                    
                    if (age <= nutrient[i][j]) {
                        nutrient[i][j] -= age;
                        trees[i][j].addLast(age + 1);
                    } else {
                        deadNutrient += age / 2;
                    }
                }
                
                nutrient[i][j] += deadNutrient;
            }
        }
    }

    static void fall() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                for (int age : trees[i][j]) {
                    if (age % 5 == 0) {
                        for (int d = 0; d < 8; d++) {
                            int nx = i + dx[d];
                            int ny = j + dy[d];
                            
                            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                                trees[nx][ny].addFirst(1);
                            }
                        }
                    }
                }
            }
        }
    }

    static void winter() {
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                nutrient[i][j] += A[i][j];
            }
        }
    }

    static int countTrees() {
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                count += trees[i][j].size();
            }
        }
        return count;
    }
}