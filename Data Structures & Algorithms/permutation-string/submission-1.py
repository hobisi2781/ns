from itertools import permutations

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        for perm in permutations(s1):
            if ''.join(perm) in s2:
                return True
        
        return False
        