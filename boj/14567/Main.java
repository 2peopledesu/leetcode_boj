import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken()); // 과목 수
        int M = Integer.parseInt(st.nextToken()); // 선수 과목 수
        
        List<List<Integer>> graph = new ArrayList<>();
        int[] inDegree = new int[N + 1]; // 진입 차수
        int[] semesters = new int[N + 1]; // 각 과목의 최소 학기 수
        
        // 그래프 초기화
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }

        // 선수 과목 관계 입력
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken()); // 선수 과목
            int b = Integer.parseInt(st.nextToken()); // 이수할 과목
            graph.get(a).add(b);
            inDegree[b]++; // b 과목의 진입 차수 증가
        }

        // 위상 정렬을 위한 큐
        Queue<Integer> queue = new LinkedList<>();

        // 진입 차수가 0인 과목을 큐에 추가
        for (int i = 1; i <= N; i++) {
            if (inDegree[i] == 0) {
                queue.offer(i);
                semesters[i] = 1; // 첫 학기
            }
        }

        // 위상 정렬 수행
        while (!queue.isEmpty()) {
            int current = queue.poll();

            for (int next : graph.get(current)) {
                inDegree[next]--; // 다음 과목의 진입 차수 감소
                semesters[next] = Math.max(semesters[next], semesters[current] + 1); // 최소 학기 수 업데이트

                if (inDegree[next] == 0) {
                    queue.offer(next); // 진입 차수가 0이 되면 큐에 추가
                }
            }
        }

        StringBuilder sb = new StringBuilder();

        // 결과 출력
        for (int i = 1; i <= N; i++) {
            sb.append(semesters[i]);
            if (i != N) {
                sb.append(" ");
            }
        }
        System.out.println(sb.toString());
    }
}