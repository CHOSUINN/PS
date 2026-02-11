import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        int ans = 0;
        int x;

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine());
        x = Integer.parseInt(st.nextToken());

        boolean[] check = new boolean[2_000_001];
        for (int i = 0; i < n; i++) {
            int targetNum = x - arr[i];
            if (targetNum >= 0 && check[targetNum]) {
                ans++;
            }
            check[arr[i]] = true;
        }
        System.out.println(ans);
    }
}