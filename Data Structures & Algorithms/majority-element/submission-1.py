class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count: dict[int, int] = defaultdict(int)
        half = len(nums) // 2
        for num in nums:
            count[num] += 1

            if count[num] > half:
                return num
        
        raise Exception('invalid input')

        