class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k
        n = len(nums)

        nums.sort(reverse=True)

        if nums[0] > target:
            return False

        memo = {}

        def solve(mask, curr_sum, count):
            # We have formed k-1 groups,
            # the remaining elements automatically form the last group.
            if count == k - 1:
                return True

            if (mask, curr_sum) in memo:
                return memo[(mask, curr_sum)]

            if curr_sum == target:
                ans = solve(mask, 0, count + 1)
                memo[(mask, curr_sum)] = ans
                return ans

            prev = -1

            for i in range(n):
                # Already used
                if mask & (1 << i):
                    continue

                # Avoid trying the same value again
                if nums[i] == prev:
                    continue

                # Can't fit in current subset
                if curr_sum + nums[i] > target:
                    continue

                prev = nums[i]

                if solve(
                    mask | (1 << i),
                    curr_sum + nums[i],
                    count
                ):
                    return True

            memo[(mask, curr_sum)] = False
            return False

        return solve(0, 0, 0)