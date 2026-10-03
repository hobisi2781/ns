class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)

        res = [0] * n

        for i in range(n):
            j = i + 1
            while j < n:
                if temperatures[i] < temperatures[j]:
                    break
                j += 1

            if j < n:
                res[i] = j - i
        
        return res
            
        