import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for (int tc = 0; tc < t; tc++) {
            boolean flag = false;
            int k = Integer.parseInt(br.readLine());

            String[] words = new String[k];
            for (int i = 0; i < k; i++) {
                words[i] = br.readLine();
            }

            for (int i = 0; i < words.length; i ++) {
                for (int j = i + 1; j < words.length; j ++) {
                    StringBuffer candidate1 = new StringBuffer(words[i] + words[j]);
                    StringBuffer candidate2 = new StringBuffer(words[j] + words[i]);

                    if (check(candidate1)) {
                        System.out.println(candidate1);
                        flag = true;
                    } else if (check(candidate2)) {
                        System.out.println(candidate2);
                        flag = true;
                    }
                    if (flag) {
                        break;
                    }
                }
                if (flag) {
                    break;
                }
            }
            if (!flag) {
                System.out.println(0);
            }
        }
    }
    
    static boolean check(StringBuffer word) {
        int left = 0;
        int right = word.length() - 1;
        
        while (left < right) {
            if (word.charAt(left) != word.charAt(right)) {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
}
