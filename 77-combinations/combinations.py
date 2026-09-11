class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def sol(st , path):
            if len(path) == k:
                res.append(path[:])
                return
            for i in range(st,n+1):
                path.append(i)
                sol(i+1 , path)
                path.pop()
        sol(1,[])
        return res

        