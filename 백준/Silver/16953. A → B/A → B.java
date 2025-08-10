import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class Main {

    static long a;
    static long b;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());

        long temp = a;
        int answer = dfs(1, temp);
        System.out.println((answer == Integer.MAX_VALUE) ? "-1" : answer);
    }

    private static int dfs(int depth, long x) {
        if (x == b) return depth;
        if (x > b) return Integer.MAX_VALUE;
        return Math.min(dfs(depth + 1, x * 2), dfs(depth + 1, x * 10 + 1));
    }
}