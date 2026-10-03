class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i = 0
        for char in s:
            if i >= len(t):
                break
            if char == t[i]:
                i += 1
        
        return len(t) - i