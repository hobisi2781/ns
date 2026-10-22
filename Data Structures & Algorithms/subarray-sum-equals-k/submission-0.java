class Solution {
    public int subarraySum(int[] nums, int k) {
        int[] prefixSum = new int[nums.length];
        int prev = 0;
        for (int i = 0; i < nums.length; i++) {
            prev += nums[i];
            prefixSum[i] = prev;
        } 

        int res = 0;

        for (int i = 0; i < prefixSum.length; i++) {
            for (int j = i; j < prefixSum.length; j++) {
                if (prefixSum[j] - prefixSum[i] + nums[i] == k) res++;
            }
        }

        return res;
    }
}