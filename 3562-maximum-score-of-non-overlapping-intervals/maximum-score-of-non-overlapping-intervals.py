
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append([l, r, w, i])

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # next[i] = first interval that starts AFTER arr[i].right
        nxt = [0] * n

        for i in range(n):
            nxt[i] = bisect_left(starts, arr[i][1] + 1)

        # dp(i, k) = best answer using intervals from i onward,
        # choosing at most k intervals.
        #
        # Store (score, indices)
        dp = [[None] * 5 for _ in range(n + 1)]

        def better(a, b):
            if a is None:
                return b
            if b is None:
                return a

            # Higher score is better
            if a[0] != b[0]:
                return a if a[0] > b[0] else b

            # Same score -> lexicographically smaller indices
            return a if a[1] < b[1] else b

        def solve(i, k):
            if i == n or k == 0:
                return (0, [])

            if dp[i][k] is not None:
                return dp[i][k]

            # Don't take this interval
            not_take = solve(i + 1, k)

            # Take this interval
            score, indices = solve(nxt[i], k - 1)

            take = (
                score + arr[i][2],
                sorted([arr[i][3]] + indices)
            )

            dp[i][k] = better(take, not_take)
            return dp[i][k]

        return solve(0, 4)[1]