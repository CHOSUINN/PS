import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    static final int NUMBER_OF_TRUCK = 3;
    static final int INPUT_INT_MAX = 100;
    static int a, b, c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        a = Integer.parseInt(st.nextToken());
        b = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());

        int[] parkingLot = new int[INPUT_INT_MAX + 1];

        for (int i = 1; i < NUMBER_OF_TRUCK + 1; i++) {
            st = new StringTokenizer(br.readLine(), " ");

            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            for (int j = x + 1; j <= y; j++) {
                parkingLot[j]++;
            }
        }

        int answer = 0;
        for (int i = 0; i < INPUT_INT_MAX + 1; i++) {
            if (parkingLot[i] > 0) {
                answer += (truckCnt(parkingLot[i]) * parkingLot[i]);
            }
        }

        System.out.println(answer);
    }

    // 트럭의 대수다 가격 반환 메서드
    private static int truckCnt (int truckCnt) {
        if (truckCnt == 1) {
            return a;
        }
        if (truckCnt == 2) {
            return b;
        }
        if (truckCnt == 3) {
            return c;
        }
        return 0;
    }
}