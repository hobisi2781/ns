from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        freq: dict[str, int] = defaultdict(int)
        for char in t:
            freq[char] += 1

        min_len = float('inf')
        min_len_start = 0

        freq_s: dict[str, int] = defaultdict(int)
        need = len(freq)
        have = 0
        i = 0
        for j in range(len(s)):
            # 1. grow
            in_char = s[j]
            freq_s[in_char] += 1

            # condition
            if in_char in freq and freq[in_char] == freq_s[in_char]:
                have += 1

            # 2. shrink 
            while have == need:
                # candidate res
                cur_len = j - i + 1
                if cur_len < min_len:
                    min_len = cur_len
                    min_len_start = i
                
                out_char = s[i]
                freq_s[out_char] -= 1

                if out_char in freq and freq[out_char] - 1 == freq_s[out_char]:
                    have -= 1
                
                i += 1

        if min_len == float('inf'):
            return '' 
        
        return s[min_len_start:min_len_start + min_len]

        