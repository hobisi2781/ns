class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]

        for i in range(1, n + 1):
            cur = i
            num_ones = 0
            while cur > i - 1:
                if cur & 1 == 1:
                    num_ones += 1
                cur = cur >> 1
            # poor man's dp
            num_ones += res[cur]
            res.append(num_ones)

        return res
        