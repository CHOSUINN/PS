class Solution {
    public int solution(int n) {
        int answer = 0;
        int nBit = Integer.bitCount(n);
        for (int i = n + 1; i < Integer.MAX_VALUE; i++) {
            int temp = Integer.bitCount(i);
            if (nBit == temp) {
                return i;
            }
        }
        return -1;
    }
}