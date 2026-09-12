class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        def solve(r , c, i):
            if i == len(word):
                return True 
            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
                return False
            t , board[r][c] =board[r][c] , "#"
            found = (
                solve ( r+1 , c , i+1) or
                solve ( r-1 , c , i+1) or
                solve ( r , c+1 , i+1) or
                solve ( r , c-1 , i+1)
            )
            board[r][c] = t
            return found
        for i in range (m):
            for j in range(n):
                if solve(i , j , 0):
                    return True
        return False

            
        