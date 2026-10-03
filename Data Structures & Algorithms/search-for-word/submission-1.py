class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        total = m * n
        
        if len(word) > total:
            return False

        def helper(coords: tuple[int,int], part:str, seen: set[tuple[int,int]]):
            i, j = coords
            # print(f"{coords=}: {part=}, {seen=}")

            if not part:
                return True
            

            dirs = [(i+1,j),(i,j+1),(i-1,j),(i,j-1)]
            for d in dirs:
                if i < 0 or j < 0 or i >= m or j >= n:
                    # print(f"{d=} out of bounds")
                    continue
                
                if board[i][j] != part[0]:
                    # print(f"{d=} char not same")
                    continue 
                    
                if d in seen:
                    # print(f"{d=} seen")
                    continue
                    
                seen.add(d)
                if helper(d, part[1:], seen):
                    return True
                seen.remove(d)
            # print(f"all fail") 
            return False

        for i in range(m):
            for j in range(n):
                if helper((i, j), word, set()):
                    return True
        return False
        