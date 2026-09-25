class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        tot = sum(nums)
        tar = 0
        if tot%2 != 0:
            return False
        tar = tot//2
        dp = [False]*(tar+1)
        dp[0] = True
        for x in nums:
            for i in range(tar,x-1,-1):
                dp[i] = dp[i] or dp[i-x]
        return dp[tar]



