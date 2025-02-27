import java.io.*;
import java.util.*;

public class Main {
    static int N;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        N = Integer.parseInt(br.readLine());
        Queue<Integer> card = new LinkedList<>();
        for (int i = 1; i <= N; i ++) {
            card.add(i);
        }
        StringBuilder result = new StringBuilder();
        for (int i = 0; i < N; i++) {
            result.append(card.poll());
            if (i < N - 1) {
                result.append(" ");
            }
            card.add(card.poll());
        }

        System.out.println(result.toString());
    }
}
