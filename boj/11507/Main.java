import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine().trim().replace("%", "");
        int[][] cards = new int[4][13];

        for (int i = 0; i < input.length(); i += 3) {
            String card = input.substring(i, i + 3);
            int card_number = Integer.parseInt(card.substring(1)) - 1;
            char card_shape = card.charAt(0);

            int shape_index;
            switch (card_shape) {
                case 'P': shape_index = 0; break; // P -> 0
                case 'K': shape_index = 1; break; // K -> 1
                case 'H': shape_index = 2; break; // H -> 2
                case 'T': shape_index = 3; break; // T -> 3
                default: continue;
            }
            if (card_number < 0 || card_number >= 13) {
                System.out.println("GRESKA");
                return;
            }

            if (cards[shape_index][card_number] != 0) {
                System.out.println("GRESKA");
                return;
            }

            cards[shape_index][card_number] = 1;
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < 4; i++) {
            result.append(13 - Arrays.stream(cards[i]).sum());
            if (i < 3) {
                result.append(" ");
            }
        }
        System.out.println(result.toString());
    }
}

