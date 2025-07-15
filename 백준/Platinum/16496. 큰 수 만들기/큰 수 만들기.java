import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        String[] arr = new String[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = st.nextToken();
        }

        Arrays.sort(arr, (a, b) -> {
            return (b + a).compareTo(a + b);
        });

        if (arr[0].equals("0")) {
            sb.append("0");
        } else {
            for (int i = 0; i < n; i++) {
                sb.append(arr[i]);
            }
        }

        System.out.println(sb);
    }
}