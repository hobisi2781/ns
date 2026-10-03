class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        smallest = nums[0]

        while l < r:
            mid = l + (r - l) // 2
            print(f"{l=}, {mid=}, {r=}")
            if nums[mid] < nums[l] and nums[mid] < nums[r]:
                l += 1
                r -= 1
            elif nums[l] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
        
        return nums[l]