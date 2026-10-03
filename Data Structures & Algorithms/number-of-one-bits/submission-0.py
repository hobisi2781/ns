class Solution:
    def hammingWeight(self, n: int) -> int:
        num_set_bits = 0
        cur = n

        while cur > 0:
            if cur & 1 == 1:
                num_set_bits += 1
            cur = cur >> 1

        return num_set_bits
        