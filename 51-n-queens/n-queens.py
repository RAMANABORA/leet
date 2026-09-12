class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."]*n for _ in range(n)]
        def issafe(row ,col):
            for i in range(row):
                if board[i][col] == "Q":
                    return False
            i , j = row -1 , col -1
            while i>=0 and j>=0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i , j = row -1 , col +1
            while i>=0 and j<n:
                if board[i][j] == "Q":
                    return False
                i-=1
                j+=1
            return True

        def sol(row ,col):
            if row == n:
                temp = ["".join(r) for r in board]
                res.append(temp)
                return 
            for col in range(n):
                if issafe(row , col):
                    board[row][col] = "Q"
                    sol(row+1 , col)
                    board[row][col] = "."
        sol(0,0)
        return res



        