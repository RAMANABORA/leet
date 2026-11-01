class Solution:
    def minMoves(self, nums: list[int]) -> int:
        m = 0 
        mi = min(nums)
        for i in nums:
            m += i- mi
        return m
        