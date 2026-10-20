class Solution {
    public int lengthOfLastWord(String s) {
        int cur = 0;
        int max = 0;    
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) != ' ') cur++;
            else cur = 0;
            if (cur > 0) max = cur;
            i++;
        }

        return max;
    }
}