import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayDeque;
import java.util.StringTokenizer;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        StringBuilder sb = new StringBuilder();

        ArrayDeque<Integer> q = new ArrayDeque<>();

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());

            switch (st.nextToken()) {
                case "push_front":
                    q.addFirst(Integer.parseInt(st.nextToken()));
                    break;
                case "push_back":
                    q.addLast(Integer.parseInt(st.nextToken()));
                    break;
                case "pop_front" :
                    if (!q.isEmpty())
                        sb.append(q.pollFirst()).append("\n");
                    else
                        sb.append(-1).append("\n");
                    break;
                case "pop_back" :
                    if (!q.isEmpty())
                        sb.append(q.pollLast()).append("\n");
                    else
                        sb.append(-1).append("\n");
                    break;
                case "size" :
                    sb.append(q.size()).append("\n");
                    break;
                case "empty" :
                    if (!q.isEmpty())
                        sb.append(0).append("\n");
                    else
                        sb.append(1).append("\n");
                    break;
                case "front" :
                    if (!q.isEmpty())
                        sb.append(q.peekFirst()).append("\n");
                    else
                        sb.append(-1).append("\n");
                    break;
                case "back" :
                    if (!q.isEmpty())
                        sb.append(q.peekLast()).append("\n");
                    else
                        sb.append(-1).append("\n");
                    break;
            }
        }
        System.out.println(sb);
    }
}