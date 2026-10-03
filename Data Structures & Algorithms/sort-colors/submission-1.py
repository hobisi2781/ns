class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        freq = [0] * 3

        for num in nums:
            freq[num] += 1
        
        j = 0
        for i in range(len(freq)):
            for _ in range(freq[i]):
                nums[j] = i
                j += 1
        