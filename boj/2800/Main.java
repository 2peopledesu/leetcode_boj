import java.util.*;

public class Main {
    static Set<String> results = new HashSet<>();
    static List<int[]> pairs = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String expression = scanner.nextLine();
        findParenthesisPairs(expression);
        generateExpressions(expression, 0, new boolean[pairs.size()]);
        
        List<String> sortedResults = new ArrayList<>(results);
        Collections.sort(sortedResults);
        for (int i = 1; i < sortedResults.size(); i++) {
            System.out.println(sortedResults.get(i));
        }
    }

    private static void findParenthesisPairs(String expression) {
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < expression.length(); i++) {
            if (expression.charAt(i) == '(') {
                stack.push(i);
            } else if (expression.charAt(i) == ')') {
                if (!stack.isEmpty()) {
                    pairs.add(new int[]{stack.pop(), i});
                }
            }
        }
    }

    private static void generateExpressions(String expression, int index, boolean[] removed) {
        if (index == pairs.size()) {
            StringBuilder newExpression = new StringBuilder(expression);
            for (int i = 0; i < pairs.size(); i++) {
                if (removed[i]) {
                    int start = pairs.get(i)[0];
                    int end = pairs.get(i)[1];
                    newExpression.setCharAt(start, ' ');
                    newExpression.setCharAt(end, ' ');
                }
            }
            results.add(newExpression.toString().replaceAll(" ", ""));
            return;
        }

        removed[index] = false;
        generateExpressions(expression, index + 1, removed);

        removed[index] = true;
        generateExpressions(expression, index + 1, removed);
    }
}