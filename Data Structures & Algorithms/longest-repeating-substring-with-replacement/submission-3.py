from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        freq: dict[str, int] = defaultdict(int)

        longest = 0
        i = 0
        cur_max_freq = 0
        for j in range(size):
            char = s[j]
            freq[char] += 1
            cur_max_freq = max(cur_max_freq, freq[char])

           # window_len = j - i + 1
            while (j - i + 1) - cur_max_freq > k:
                freq[s[i]] -= 1
                i += 1
            
            longest = max(longest, j - i + 1)

        return longest

        