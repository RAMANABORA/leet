class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def solve(o , c ,path):
            if len(path) == 2*n:
                res.append("".join(path))    
                return
            if o<n:
                path.append("(")
                solve(o+1 , c ,path)
                path.pop()
            if c<o:
                path.append(")")
                solve(o , c+1 , path)
                path.pop()
        solve(0 ,0 ,[])
        return res
        