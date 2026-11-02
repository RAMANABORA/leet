class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        m = 0
        if len(nums)==1:
            return 0
        else :
            mi = nums[len(nums)//2]
        for i in nums:
            m += abs(i-mi)
        return m

        
        