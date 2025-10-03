import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        char[] arr = br.readLine().toCharArray();

        for (int i = 0; i < arr.length; i++) {
            sb.append(rot13(arr[i]));
        }
        System.out.println(sb);
    }

    private static char rot13(char a) {
        if (a >= 'a' && a <= 'z') {
            return (char) (((a - 'a' + 13) % 26) + 'a');
        }
        if ('A' <= a && a <= 'Z') {
            return (char) (((a - 'A' + 13) % 26) + 'A');
        }
        return a;
    }
}