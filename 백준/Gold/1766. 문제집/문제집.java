import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        List<List<Integer>> queue = new ArrayList<>();

        for (int i = 0; i < n + 1; i++)
            queue.add(new ArrayList<>());

        int[] ezNums = new int[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            queue.get(a).add(b);
            ezNums[b]++;
        }

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int i = 1; i < n + 1; i++) {
            if (ezNums[i] == 0) {
                pq.add(i);
            }
        }

        while (!pq.isEmpty()) {
            int temp = pq.poll();
            sb.append(temp).append(" ");

            for (int i = 0; i < queue.get(temp).size(); i++) {
                ezNums[queue.get(temp).get(i)]--;
                if (ezNums[queue.get(temp).get(i)] == 0)
                    pq.add(queue.get(temp).get(i));
            }
        }
        System.out.println(sb);
    }
}