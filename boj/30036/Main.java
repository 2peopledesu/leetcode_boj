import java.io.*;
import java.util.*;

public class Main {

    static int[] dy = {-1, 1, 0, 0};
    static int[] dx = {0, 0, -1, 1};

    public static boolean isInRange(int y, int x, int n, char[][] graph) {
        return y >= 0 && y < n && x >= 0 && x < n && 
               graph[y][x] != '#' && !Character.isUpperCase(graph[y][x]);
    }

    public static class Square {
        private int y, x;
        private int ink = 0;

        public void setPosition(int y, int x) {
            this.y = y;
            this.x = x;
        }

        public int getY() {
            return y;
        }

        public int getX() {
            return x;
        }

        public int getInk() {
            return ink;
        }

        public void setInk(int ink) {
            this.ink = ink;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int i = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        String ink = br.readLine();

        char[][] graph = new char[n][n];

        Square square = new Square();

        for (int j = 0; j < n; j++) {
            String line = br.readLine();
            for (int l = 0; l < n; l++) {
                char now = line.charAt(l);
                if (now == '@') {
                    square.setPosition(j, l);
                    graph[j][l] = '.';
                } else {
                    graph[j][l] = now;
                }
            }
        }

        String command = br.readLine();

        for (int j = 0; j < k; j++) {
            char nowCommend = command.charAt(j);

            switch (nowCommend) {
                case 'U':
                    if (isInRange(square.getY() - 1, square.getX(), n, graph)) {
                        square.setPosition(square.getY() - 1, square.getX());
                    }
                    break;
                case 'D':
                    if (isInRange(square.getY() + 1, square.getX(), n, graph)) {
                        square.setPosition(square.getY() + 1, square.getX());
                    }
                    break;
                case 'L':
                    if (isInRange(square.getY(), square.getX() - 1, n, graph)) {
                        square.setPosition(square.getY(), square.getX() - 1);
                    }
                    break;
                case 'R':
                    if (isInRange(square.getY(), square.getX() + 1, n, graph)) {
                        square.setPosition(square.getY(), square.getX() + 1);
                    }
                    break;
                case 'j':
                    square.setInk(square.getInk() + 1);
                    break;
                case 'J':
                    if (square.getInk() > 0) {
                        int jumpCount = 0;
                        for (int m = 0; m < j; m++) {
                            if (command.charAt(m) == 'J') jumpCount++;
                        }
                        jumpCount++;
                        char inkColor = ink.charAt((jumpCount - 1) % i);
                        
                        int inkAmount = square.getInk();
                        int squareY = square.getY();
                        int squareX = square.getX();
                        
                        for (int y = 0; y < n; y++) {
                            for (int x = 0; x < n; x++) {
                                if ((graph[y][x] == '#' || Character.isUpperCase(graph[y][x])) && 
                                    Math.abs(y - squareY) + Math.abs(x - squareX) <= inkAmount) {
                                    graph[y][x] = inkColor;
                                }
                            }
                        }
                        
                        square.setInk(0);
                    }
                    break;
            }
        }
        
        for (int y = 0; y < n; y++) {
            for (int x = 0; x < n; x++) {
                if (y == square.getY() && x == square.getX()) {
                    System.out.print("@");
                } else {
                    System.out.print(graph[y][x]);
                }
            }
            System.out.println();
        }
    }
}
