class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k

        # dp[r] = number of subarrays ending at previous position
        # whose product % k == r
        dp = [0] * k

        for num in nums:
            val = num % k
            new_dp = [0] * k

            # Start a new subarray with num
            new_dp[val] += 1

            # Extend previous subarrays
            for r in range(k):
                new_r = (r * val) % k
                new_dp[new_r] += dp[r]

            dp = new_dp

            # Add current subarrays to result
            for r in range(k):
                result[r] += dp[r]

        return result