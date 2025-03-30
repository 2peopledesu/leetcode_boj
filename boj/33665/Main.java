import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        
        int [][] cities = new int[10][4];

        for (int i = 0; i < 10; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 4; j++) {
                cities[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        String cityOwner = br.readLine();

        String proposal = br.readLine();

        String mortgage = br.readLine();

        int myCash = Integer.parseInt(br.readLine());
        int otherCash = Integer.parseInt(br.readLine());

        int myProposalCash = Integer.parseInt(br.readLine());
        int otherProposalCash = Integer.parseInt(br.readLine());

        int weight = Integer.parseInt(br.readLine());
        int panelty = Integer.parseInt(br.readLine());

        int[][] beforeCityOwner = new int[2][10];
        int[][] beforeMortgage = new int[2][10];

        for (int i = 0; i < 40; i++) {
            int color = i / 4 ;
            char owner = cityOwner.charAt(i);
            char tempMortgage = mortgage.charAt(i);

            if (owner == '1') {
                beforeCityOwner[0][color]++;
                if (tempMortgage == '1') {
                    beforeMortgage[0][color]++;
                }
            } else if (owner == '2') {
                beforeCityOwner[1][color]++;
                if (tempMortgage == '1') {
                    beforeMortgage[1][color]++;
                }
            }
        }

        int[][] afterCityOwner = new int[2][10];
        int[][] afterMortgage = new int[2][10];
        
        for (int i = 0; i < 2; i++) {
            for (int j = 0; j < 10; j++) {
                afterCityOwner[i][j] = beforeCityOwner[i][j];
                afterMortgage[i][j] = beforeMortgage[i][j];
            }
        }

        for (int i = 0; i < 40; i++) {
            int color = i / 4;
            char owner = cityOwner.charAt(i);
            char proposer = proposal.charAt(i);
            char tempMortgage = mortgage.charAt(i);

            if (proposer == '1' && owner == '2') {
                afterCityOwner[0][color]++;
                afterCityOwner[1][color]--;
                if (tempMortgage == '1') {
                    afterMortgage[0][color]++;
                    afterMortgage[1][color]--;
                }
            } else if (proposer == '2' && owner == '1') {
                afterCityOwner[1][color]++;
                afterCityOwner[0][color]--;
                if (tempMortgage == '1') {
                    afterMortgage[1][color]++;
                    afterMortgage[0][color]--;
                }
            }
        }

        int afterMyCash = myCash - myProposalCash + otherProposalCash;
        int afterOtherCash = otherCash - otherProposalCash + myProposalCash;

        int beforeMyValue = calculateCash(beforeCityOwner[0], beforeMortgage[0], myCash, cities, weight, panelty);
        int beforeOtherValue = calculateCash(beforeCityOwner[1], beforeMortgage[1], otherCash, cities, weight, panelty);

        int afterMyValue = calculateCash(afterCityOwner[0], afterMortgage[0], afterMyCash, cities, weight, panelty);
        int afterOtherValue = calculateCash(afterCityOwner[1], afterMortgage[1], afterOtherCash, cities, weight, panelty);
     
        int beforeTrade = beforeMyValue - beforeOtherValue;
        int afterTrade = afterMyValue - afterOtherValue;

        if (afterTrade >= beforeTrade) {
            System.out.println("YES");
        } else {
            System.out.println("NO");
        }
    }

    private static int calculateCash(int[] owner, int[] mortgage, int cash, int[][] cities, int weight, int panelty) {
        int result = 0;

        for (int i = 0; i < 10; i++) {
            if (owner[i] > 0) {
                result += cities[i][owner[i] - 1];
            }
        }

        result += (cash * weight) / 100;

        int totalMortgage = 0;
        for (int i = 0; i < 10; i++) {
            totalMortgage += mortgage[i];
        }

        result -= (totalMortgage * panelty);

        return result;
    }
    
}
