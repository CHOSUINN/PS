import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Node {
    int num;
    Node left;
    Node right;

    public Node(int a) {
        num = a;
    }
}
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        Node root = new Node(Integer.parseInt(br.readLine()));

        String line;
        while ((line = br.readLine()) != null) {
            int num = Integer.parseInt(line);
            insertNode(root, num);
        }
        postOrder(root);
    }

    private static void postOrder(Node root) {
        if (root.left != null) {
            postOrder(root.left);
        }

        if (root.right != null) {
            postOrder(root.right);
        }

        System.out.println(root.num);
    }

    public static void insertNode(Node curr, int v) {

        if (curr.num > v) {
            if (curr.left == null) {
                curr.left = new Node(v);
            } else {
                insertNode(curr.left, v);
            }
        } else {
            if (curr.right == null) {
                curr.right = new Node(v);
            } else {
                insertNode(curr.right, v);
            }
        }
    }
}