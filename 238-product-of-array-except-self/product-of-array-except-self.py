class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        t = 1
        c = 0
        ans = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                c += 1
            else:
                t *= nums[i]
        if c > 1:
            return ans
        elif c == 1:
            for i in range(len(nums)):
                if nums[i] == 0:
                    ans[i] = t
            return ans
        else:
            for i in range(len(nums)):
                ans[i] = t // nums[i]
            return ans