class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        m = amount+1
        dp = [m]*(m)
        dp[0] = 0
        if amount == 0:
            return  0
        for c in coins:
            for i in range(c , m):
                dp[i] = min(dp[i] , dp[i-c]+1)
        return dp[amount] if dp[amount]!=m else -1



        