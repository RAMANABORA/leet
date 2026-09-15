class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        pal = [[False] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 1 or pal[i + 1][j - 1]):
                    pal[i][j] = True
        dp = [0] * (n + 1)
        for i in range(n):
            dp[i + 1] = dp[i]
            for l in range(i + 1):
                if i - l + 1 >= k and pal[l][i]:
                    dp[i + 1] = max(dp[i + 1], dp[l] + 1)
        return dp[n]