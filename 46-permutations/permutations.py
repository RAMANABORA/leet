class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        mp = [0]*len(nums)
        def sol(path):
            if len(nums) == len(path):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if mp[i]:
                    continue
                path.append(nums[i])
                mp[i]+=1
                sol(path)
                path.pop()
                mp[i]-=1
        sol([])
        return res        