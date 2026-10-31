class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        relen = 0
        for i in range(len(s)):
            # Odd
            l = i
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > relen:
                    relen = length
                    res = s[l:r+1]
                l -= 1
                r += 1
            # Even
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > relen:
                    relen = length
                    res = s[l:r+1]
                l -= 1
                r += 1
        return res