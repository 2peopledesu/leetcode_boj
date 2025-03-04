import java.io.*;
import java.util.*;

public class Main {
    static int N, M, K;
    static int[][] originalArray;
    static int[][] rotateInfo;
    static int[] order;
    static boolean[] visited;
    static int minValue = Integer.MAX_VALUE;
    
    public static int[][] rotate(int[][] array, int r, int c, int s) {
        int[][] newArray = new int[N][M];

        for(int i = 0; i < N; i++) {
            newArray[i] = array[i].clone();
        }
        
        for(int i = 1; i <= s; i++) {

            int startX = r-i;
            int startY = c-i;
            int endX = r+i;
            int endY = c+i;
            
            int temp = newArray[startX][startY];
            
            for(int j = startX; j < endX; j++) {
                newArray[j][startY] = newArray[j+1][startY];
            }
            for(int j = startY; j < endY; j++) {
                newArray[endX][j] = newArray[endX][j+1];
            }
            for(int j = endX; j > startX; j--) {
                newArray[j][endY] = newArray[j-1][endY];
            }
            for(int j = endY; j > startY; j--) {
                newArray[startX][j] = newArray[startX][j-1];
            }
            newArray[startX][startY+1] = temp;
        }
        return newArray;
    }
    
    public static int calculateArrayValue(int[][] array) {
        int minSum = Integer.MAX_VALUE;
        for(int i = 0; i < N; i++) {
            int sum = 0;
            for(int j = 0; j < M; j++) {
                sum += array[i][j];
            }
            minSum = Math.min(minSum, sum);
        }
        return minSum;
    }
    
    public static void permutation(int depth) {
        if(depth == K) {
            int[][] currentArray = new int[N][M];
           
            for(int i = 0; i < N; i++) {
                currentArray[i] = originalArray[i].clone();
            }
            
            for(int i = 0; i < K; i++) {
                int[] current = rotateInfo[order[i]];
                currentArray = rotate(currentArray, current[0]-1, current[1]-1, current[2]);
            }
            
            minValue = Math.min(minValue, calculateArrayValue(currentArray));
            return;
        }
        
        for(int i = 0; i < K; i++) {
            if(!visited[i]) {
                visited[i] = true;
                order[depth] = i;
                permutation(depth + 1);
                visited[i] = false;
            }
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());
        
        originalArray = new int[N][M];
        rotateInfo = new int[K][3];
        order = new int[K];
        visited = new boolean[K];
        
        for(int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < M; j++) {
                originalArray[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        
        for(int i = 0; i < K; i++) {
            st = new StringTokenizer(br.readLine());
            rotateInfo[i][0] = Integer.parseInt(st.nextToken());
            rotateInfo[i][1] = Integer.parseInt(st.nextToken());
            rotateInfo[i][2] = Integer.parseInt(st.nextToken());
        }
        
        permutation(0);
        System.out.println(minValue);
    }
}