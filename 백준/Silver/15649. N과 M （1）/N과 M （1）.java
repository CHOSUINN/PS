import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static int[] arr1;
    static int[] arr2;
    static boolean[] visited;
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr1 = new int[n];
        arr2 = new int[m];
        visited = new boolean[n];

        for (int i = 0; i < n; i++)
            arr1[i] = i + 1;

        dfs(0);
    }

    private static void dfs(int depth) {

        if (depth == m) {
            for (int n : arr2) {
                System.out.print(n + " ");
            }
            System.out.println();
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                arr2[depth] = i + 1;
                dfs(depth + 1);
                visited[i] = false;
            }
        }
    }
}