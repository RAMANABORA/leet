class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        def solve(st , path , rem):
            if len(path) == k:
                if rem == 0:
                    res.append(path.copy())
                    return
            for i in range(st , 10):
                if i > n:
                    break
                path.append(i)
                solve(i+1 ,path ,rem - i)
                path.pop()
        solve(1 ,[] , n)
        return res

        