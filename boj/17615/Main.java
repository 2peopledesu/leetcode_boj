import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String balls = br.readLine();

        int totalRed = 0;
        for (int i = 0; i < n; i++) {
            if (balls.charAt(i) == 'R') totalRed++;
        }
        int totalBlue = n - totalRed;
        
        int minMoves = n;
        
        int continuousRed = countContinuousBalls(balls, 'R', true);
        minMoves = Math.min(minMoves, totalRed - continuousRed);
        
        continuousRed = countContinuousBalls(balls, 'R', false);
        minMoves = Math.min(minMoves, totalRed - continuousRed);
        
        int continuousBlue = countContinuousBalls(balls, 'B', true);
        minMoves = Math.min(minMoves, totalBlue - continuousBlue);
        
        continuousBlue = countContinuousBalls(balls, 'B', false);
        minMoves = Math.min(minMoves, totalBlue - continuousBlue);
        
        System.out.println(minMoves);
    }
    
    private static int countContinuousBalls(String balls, char color, boolean fromLeft) {
        int count = 0;
        int n = balls.length();
        
        if (fromLeft) {
            for (int i = 0; i < n; i++) {
                if (balls.charAt(i) == color) count++;
                else break;
            }
        } else {
            for (int i = n - 1; i >= 0; i--) {
                if (balls.charAt(i) == color) count++;
                else break;
            }
        }
        
        return count;
    }
}