class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def check (x):
            return x == x[::-1]
        def solve(st ,path):
            if st == len(s):
                res.append(path.copy())
                return 
            for i in range (st , len(s)):
                if check(s[st:i+1]):
                    path.append(s[st:i+1])
                    solve(i+1 , path)
                    path.pop()
        solve(0,[])
        return res