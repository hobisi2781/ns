class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        size = len(s)
        i = 0
        longest = 1
        chars: set[str] = set([s[0]])

        for j in range(1, size):
            if s[j] in chars:
                while s[j] in chars:
                    chars.remove(s[i])
                    i += 1
        
            chars.add(s[j])
            
            cur_size = len(chars)
            if cur_size > longest:
                longest = cur_size

        return longest
        