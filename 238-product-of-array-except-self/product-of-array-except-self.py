
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n
        pm = 1
        for i in range(n):
            ans[i] = pm
            pm *= nums[i]
        sm = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= sm
            sm *= nums[i]
        return ans
