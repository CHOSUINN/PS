import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] a = new int[26];
        int[] b = new int[26];
        int cnt = 0;

        String one = st.nextToken();
        String two = br.readLine();

        for (int i = 0; i < one.length(); i++) {
            a[one.charAt(i) - 'a']++;
        }

        for (int i = 0; i < two.length(); i++) {
            b[two.charAt(i) - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (a[i] > b[i]) {
                while (a[i] > b[i]) {
                    a[i]--;
                    cnt++;
                }
            }

            if (a[i] < b[i])
            while (a[i] < b[i]) {
                b[i]--;
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}