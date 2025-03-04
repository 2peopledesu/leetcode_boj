import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().trim();
        Set<String> result = new HashSet<>();
        generatePermutations("", input, result);

        List<String> sortedPermutations = new ArrayList<>(result);
        Collections.sort(sortedPermutations);

        for (int i = 0; i < sortedPermutations.size(); i++) {
            if (sortedPermutations.get(i).equals(input)) {
                if (i == sortedPermutations.size() - 1) {
                    System.out.println(0);
                } else {
                    System.out.println(sortedPermutations.get(i + 1));
                }
                return;
            }
        }
    }

    private static void generatePermutations(String prefix, String str, Set<String> result) {
        int n = str.length();
        if (n == 0) {
            result.add(prefix);
        } else {
            for (int i = 0; i < n; i++) {
                generatePermutations(prefix + str.charAt(i), str.substring(0, i) + str.substring(i + 1), result);
            }
        }
    }
}
