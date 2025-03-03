import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split("");
        Arrays.sort(input, Collections.reverseOrder());
        System.out.println(String.join("", input));
    }
}
