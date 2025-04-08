import java.io.*;
import java.util.*;

public class Main {
    static int n, m, r;
    static int[] dx = {-1, 0, 0, 1};
    static int[] dy = {0, -1, 1, 0};
    static int[][] map;
    static char[][] result;
    static Stack<int[]> attackStack;
    static int resultCount = 0;

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        r = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        for(int i = 0; i < n; i++){
            st = new StringTokenizer(br.readLine());
            for(int j = 0; j < m; j++){
                map[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        result = new char[n][m];
        for(int i = 0; i < n; i++){
            Arrays.fill(result[i], 'S');
        }

        for(int i = 0; i < r; i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            char d = st.nextToken().charAt(0);

            x--;
            y--;
            
            if (result[x][y] == 'S') {
                int dirIndex = -1;
                switch(d) {
                    case 'N': dirIndex = 0; break;
                    case 'W': dirIndex = 1; break;
                    case 'E': dirIndex = 2; break;
                    case 'S': dirIndex = 3; break;
                }

                attackStack = new Stack<>();
                attackStack.add(new int[] {x, y, dirIndex});
                while(!attackStack.isEmpty()){
                    int[] attack = attackStack.pop();
                    doAttack(attack[0], attack[1], attack[2]);
                }
                
                st = new StringTokenizer(br.readLine());
                int defenceX = Integer.parseInt(st.nextToken());
                int defenceY = Integer.parseInt(st.nextToken());

                defenceX--;
                defenceY--;

                if(result[defenceX][defenceY] == 'F'){
                    result[defenceX][defenceY] = 'S';
                }
            }
        }
        System.out.println(resultCount);
        for(int i = 0; i < n; i++){
            for(int j = 0; j < m; j++){
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
    public static void doAttack(int x, int y, int dirIndex){
        int ag = map[x][y];

        for (int j = 0; j < ag; j++){
            int nx = x + (dx[dirIndex] * j);
            int ny = y + (dy[dirIndex] * j);

            if(nx >= 0 && nx < n && ny >= 0 && ny < m){
                if(result[nx][ny] == 'S'){
                    attackStack.add(new int[] {nx, ny, dirIndex});
                    result[nx][ny] = 'F';
                    resultCount++;
                }
            }
        }
    }
}