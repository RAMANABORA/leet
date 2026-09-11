class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        mpp=[0]*len(nums)
        def sol(path):
            if len(nums) == len(path):
                res.append(path.copy())
                return
            for i in range(len(nums)):
                if mpp[i]:
                    continue
                if i >0 and nums[i] == nums[i-1] and mpp[i-1] == 0:
                    continue
                path.append(nums[i])
                mpp[i]+=1
                sol(path)
                path.pop()
                mpp[i]-=1
        sol([])
        return res
        