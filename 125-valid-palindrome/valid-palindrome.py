class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for l in s:
            if l.isalnum():
                res += l.lower()
        return res == res[::-1]
            
