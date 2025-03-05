import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();
        
        char[] duck = {'q', 'u', 'a', 'c', 'k'};
        boolean[] visited = new boolean[input.length()];
        int minduck = 0;

        if (input.length() % 5 != 0 ||input.charAt(0) != 'q') {
            System.out.println(-1);
            return;
        }

        for (int i = 0; i < input.length(); i++) {
            if (visited[i]) continue;
            if (input.charAt(i) == 'q') {
                visited[i] = true;
                int index = 1;
                int QuackCount = 1;
                for (int j = i + 1; j < input.length(); j++) {
                    if (!visited[j] && input.charAt(j) == duck[index]) {
                        visited[j] = true;
                        index = (index + 1) % 5;
                        QuackCount++;
                    }
                }
                if (QuackCount != 0 &&QuackCount % 5 == 0) minduck++;
                else {
                    System.out.println(-1);
                    return;
                }
            }
        }
        System.out.println(minduck);
    }
}