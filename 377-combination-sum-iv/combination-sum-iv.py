class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        c = 0
        dp = [0]*(target+1)
        dp[0] = 1
        for i in range(target+1):
            for x in nums:
                if x<=i :
                    dp[i] += dp[i-x]
        return dp[target]


