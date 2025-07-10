import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());

        int[][] arr = new int[n][3];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < 3; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        int[] dp1 = new int[n];
        int[] dp2 = new int[n];
        int[] dp3 = new int[n];

        dp1[0] = arr[0][0];
        dp2[0] = arr[0][1];
        dp3[0] = arr[0][2];

        for (int i = 1; i < n; i++) {
            dp1[i] = arr[i][0] + Math.min(dp2[i - 1], dp3[i - 1]);
            dp2[i] = arr[i][1] + Math.min(dp1[i - 1], dp3[i - 1]);
            dp3[i] = arr[i][2] + Math.min(dp1[i - 1], dp2[i - 1]);
        }

        int answer = min(dp1[n - 1], dp2[n - 1], dp3[n - 1]);
        System.out.println(answer);
    }

    static int min(int... input) {
        int minVal = 2147483647;
        for (int i = 0; i < input.length; i++) {
            if (input[i] < minVal) {
                minVal = input[i];
            }
        }
        return minVal;
    }
}
