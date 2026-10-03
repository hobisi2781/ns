class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0) return 0;

        Set<Integer> seen = new HashSet<>(); 

        for (int num: nums) {
            seen.add(num);
        }

        int longest = 0;

        for (int num: nums) {
            if (seen.contains(num - 1)) continue;
            int cur = 0;

            while (seen.contains(num)) {
                num++;
                cur++;
            }

            longest = Math.max(cur, longest);

        }

        return longest;
        
    }
}
