class Solution:
    def validPalindrome(self, nums: str) -> bool:
        n = len(nums)
        l = 0
        r = n-1
        def check(l, r):
            while l < r:
                if nums[l] != nums[r]:
                    return False
                l += 1
                r -= 1
            return True
        while l < r:
            if nums[l] != nums[r]:
                return check(l, r-1) or check(l+1, r)
            l += 1
            r -= 1
        return True
