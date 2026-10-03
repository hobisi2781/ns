import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res: list[int] = []
        heap: list[tuple[int, int]] = []

        n = len(nums)

        for i in range(n):
            num = nums[i]
            heapq.heappush(heap, (-num, i))

            j = i - k

            if j + 1 < 0:
                continue
            
            while heap[0][1] <= j:
                heapq.heappop(heap)

            res.append(-heap[0][0])

        return res
        