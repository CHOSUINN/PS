import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        long a = Long.parseLong(st.nextToken());
        long b = Long.parseLong(st.nextToken());
        long c = Long.parseLong(st.nextToken());

        long answer = cal(a, b, c);
        System.out.println(answer);
    }

    private static long cal(long a, long b, long c) {
        long base = a % c;
        long result = 1 % c;

        while (b > 0) {
            if ((b & 1) == 1) {
                result = (result * base) % c;
            }
            base = (base * base) % c;
            b >>= 1;
        }
        return result;
    }
}