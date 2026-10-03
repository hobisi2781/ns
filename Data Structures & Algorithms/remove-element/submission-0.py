class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        size = len(nums)
        clean_until = 0

        for i in range(size):
            if nums[i] == val:
                continue
            nums[clean_until], nums[i] = nums[i], nums[clean_until]
            clean_until += 1

        return clean_until
        