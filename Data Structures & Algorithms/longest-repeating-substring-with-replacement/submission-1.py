class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        size = len(s)
        longest = 0
        for char in set(s):
            used = 0
            i = 0
            for j in range(size):
                if char != s[j]:
                    used += 1
                
                while used > k:
                    if char != s[i]:
                        used -= 1
                    i += 1
                
                cur = j - i + 1
                if cur > longest:
                    longest = cur
        
        return longest

        