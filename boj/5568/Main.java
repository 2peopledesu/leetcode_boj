import java.io.*;
import java.util.*;

public class Main {
    static int n, k;
    static int[] cards;
    static Set<Integer> uniqueNumbers = new HashSet<>();
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        cards = new int[n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            cards[i] = Integer.parseInt(br.readLine());
        }

        generatePermutations(0, new StringBuilder());
        System.out.println(uniqueNumbers.size());
    }

    static void generatePermutations(int depth, StringBuilder current) {
        if (depth == k) {
            int number = Integer.parseInt(current.toString());
            uniqueNumbers.add(number);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                String numStr = String.valueOf(cards[i]);
                current.append(numStr);

                generatePermutations(depth + 1, current);

                current.delete(current.length() - numStr.length(), current.length());
                visited[i] = false;
            }
        }
    }
}