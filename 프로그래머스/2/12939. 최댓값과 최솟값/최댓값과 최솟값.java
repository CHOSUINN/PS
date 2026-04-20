import java.util.*;

class Solution {
    public String solution(String s) {
        StringBuilder sb = new StringBuilder();
        StringTokenizer st = new StringTokenizer(s, " ");
        
        int maxNum = -2147483648;
        int minNum = 2147483647;
        while (st.hasMoreTokens()) {
            int temp  = Integer.parseInt(st.nextToken());
            if (maxNum < temp)
                maxNum = temp;
            if (minNum > temp)
                minNum = temp;
        }
        
        return minNum + " " + maxNum;
    }
}