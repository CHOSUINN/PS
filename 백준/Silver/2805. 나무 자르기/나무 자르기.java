import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        long m = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);

        long lt = 0;
        long rt = arr[n - 1];
        long mid = lt + (rt - lt) / 2;
        long answer = 0;
        while (lt <= rt) {
            long sum = 0;
            for (int i = 0; i < n; i++) {
                if (mid < arr[i]) {
                    sum += (arr[i] - mid);
                }
            }

            if (sum < m) {
                rt = mid - 1;
            } else {
                answer = mid;
                lt = mid + 1;
            }
            mid = lt + (rt - lt) / 2;

        }

        System.out.println(answer);

    }
}

