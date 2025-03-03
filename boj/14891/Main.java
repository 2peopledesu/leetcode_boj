import java.io.*;
import java.util.*;

public class Main {
    public static void rotateSingleGear(int[] gear, int direction) {
        if (direction == 1) {
            int temp = gear[7];
            for (int i = 7; i > 0; i--) {
                gear[i] = gear[i-1];
            }
            gear[0] = temp;
        } else if (direction == -1) {
            int temp = gear[0];
            for (int i = 0; i < 7; i++) {
                gear[i] = gear[i+1];
            }
            gear[7] = temp;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int[][] gears = new int[4][8];
        for (int i = 0; i < 4; i++) {
            String input = br.readLine();
            for (int j = 0; j < 8; j++) {
                gears[i][j] = input.charAt(j) - '0';
            }
        }

        int k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int gearNum = Integer.parseInt(st.nextToken()) - 1;
            int direction = Integer.parseInt(st.nextToken());
            
            int[] rotateDirections = new int[4];
            rotateDirections[gearNum] = direction;
            
            for (int j = gearNum; j > 0; j--) {
                if (gears[j][6] != gears[j-1][2]) {
                    rotateDirections[j-1] = -rotateDirections[j];
                } else {
                    break;
                }
            }
            
            for (int j = gearNum; j < 3; j++) {
                if (gears[j][2] != gears[j+1][6]) {
                    rotateDirections[j+1] = -rotateDirections[j];
                } else {
                    break;
                }
            }
            
            for (int j = 0; j < 4; j++) {
                if (rotateDirections[j] != 0) {
                    rotateSingleGear(gears[j], rotateDirections[j]);
                }
            }
        }
        
        int score = 0;
        for (int i = 0; i < 4; i++) {
            if (gears[i][0] == 1) {
                score += (1 << i);
            }
        }
        System.out.println(score);
    }
}