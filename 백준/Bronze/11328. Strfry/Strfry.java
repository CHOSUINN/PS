import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{
    
    private static boolean ft_strfry(String a, String b) {
        if (a.length() != b.length()) {
            return false;
        }
        int[] alpha = new int[26];
        for (int i = 0; i < a.length(); i++) {
            alpha[a.charAt(i) - 'a']++;
        }
        for (int i = 0; i < b.length(); i++) {
            if (alpha[b.charAt(i) - 'a'] - 1 < 0)
                return false;
            alpha[b.charAt(i) - 'a']--;
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int tc = Integer.parseInt(st.nextToken());
        for (int t = 0; t < tc; t++) {
            st = new StringTokenizer(br.readLine());
            String a = st.nextToken();
            String b = st.nextToken();

            if (ft_strfry(a, b)) {
                sb.append("Possible").append('\n');
            } else {
                sb.append("Impossible").append('\n');
            }
        }
        System.out.println(sb);
    }
}