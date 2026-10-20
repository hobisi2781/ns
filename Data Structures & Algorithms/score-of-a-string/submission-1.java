class Solution {
    public int scoreOfString(String s) {
        int res = 0;
        for (int i = 1; i < s.length(); i++) {
            int diff = Character.codePointAt(s, i) - Character.codePointAt(s, i-1);
            res += Math.abs(diff);
        }

        return res;
    }
}