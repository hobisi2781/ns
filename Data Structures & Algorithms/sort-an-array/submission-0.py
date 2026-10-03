class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums
    

    def mergeSort(self, nums: list[int], lo: int, hi: int):

        if lo < hi:
            mid = lo + (hi - lo) // 2
            self.mergeSort(nums, lo, mid)
            self.mergeSort(nums, mid + 1, hi)
            self.merge(nums, lo, mid, hi)

    

    def merge(self, nums: list[int], lo: int, mid: int, hi: int):
        left = nums[lo:mid+1]
        right = nums[mid+1:hi+1]

        i = 0; j = 0; k = lo

        while i < (mid - lo + 1) and j < (hi - mid):
            if left[i] <= right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
        
            k += 1

        while i < (mid - lo + 1):
            nums[k] = left[i]
            i += 1
            k += 1
        
        while j < (hi - mid):
            nums[k] = right[j]
            j += 1
            k += 1
        