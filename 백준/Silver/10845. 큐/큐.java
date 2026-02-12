import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

class Node {
    int val;
    Node right;

    Node(int val) {
        this.val = val;
        this.right = null;
    }
}

public class Main{

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        Node head = null;
        Node curr = null;
        int size = 0;

        int n = Integer.parseInt(st.nextToken());
        for (int i = 0; i < n; i++) {
            String[] input = br.readLine().split(" ");
            switch (input[0]) {
                case "push":
                    Node temp = new Node(Integer.parseInt(input[1]));
                    if (curr == null) {
                        head = temp;
                        curr = temp;
                    } else {
                        curr.right = temp;
                        curr = temp;
                    }
                    size++;
                    break;
                case "pop" :
                    if (head == null) {
                        System.out.println(-1);
                    } else {
                        System.out.println(head.val);
                        head = head.right;
                        size--;

                        if (head == null) {
                            curr = null;
                        }
                    }
                    break;
                case "size" :
                    System.out.println(size);
                    break;
                case "empty":
                    if (size == 0) {
                        System.out.println(1);
                    } else {
                        System.out.println(0);
                    }
                    break;
                case "front":
                    if (size > 0)
                        System.out.println(head.val);
                    else
                        System.out.println(-1);
                    break;
                case "back" :
                    if (size > 0)
                        System.out.println(curr.val);
                    else
                        System.out.println(-1);
                    break;
            }
        }
    }
}