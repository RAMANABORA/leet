class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m = 0
        mi = max(nums)
        for i in nums:
            m += mi - i
        return m 

        