import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        String input = st.nextToken();
        int[] numSet = new int[10];
        int sixNine = 0;
        int maxNumSet = 0;
        int maxNumSetCnt = 0;
        for (int i = 0; i < input.length(); i++) {
            int temp = Integer.parseInt(String.valueOf(input.charAt(i)));
            if (temp == 6 || temp == 9)
                sixNine++;
            else
                numSet[temp]++;
        }

        for (int i = 0; i < numSet.length; i++) {
            if (maxNumSetCnt < numSet[i]) {
                maxNumSetCnt = numSet[i];
                maxNumSet = i;
            }
        }

        int sixNineCnt = 0;
        if (sixNine % 2 == 1) {
            sixNineCnt = sixNine / 2 + 1;
        } else {
            sixNineCnt = sixNine / 2;
        }

        if (sixNineCnt < maxNumSetCnt) {
            System.out.println(maxNumSetCnt);
        } else {
            System.out.println(sixNineCnt);
        }
    }
}