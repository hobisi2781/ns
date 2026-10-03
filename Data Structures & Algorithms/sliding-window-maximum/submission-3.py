from collections import defaultdict
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res: list[int] = []
        freq: dict[int, int] = defaultdict(int)

        n = len(nums)
        cur_max = float('-inf')

        for i in range(k):
            freq[nums[i]] += 1
            if nums[i] > cur_max:
                cur_max = nums[i]
        
        res.append(cur_max)
        
        for r in range(k, n):
            l = r - k
            in_num = nums[r]
            out_num = nums[l]

            freq[in_num] += 1
            freq[out_num] -= 1
            if freq[out_num] <= 0:
                del freq[out_num]

            if out_num == cur_max:
                cur_max = float('-inf')
                for num in freq:
                    if num > cur_max:
                        cur_max = num
            elif in_num > cur_max:
                cur_max = in_num
            res.append(cur_max)

            

        return res
        