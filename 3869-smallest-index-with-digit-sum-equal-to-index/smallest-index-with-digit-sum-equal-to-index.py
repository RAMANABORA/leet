class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        i = 0
        temp = 0
        n = len(nums)
        if n < 1:
            return 0

        while i<n:
            temp = nums[i]
            sm = 0
            while temp >0:
                dig = temp%10
                sm+=dig
                temp //=10
            if i == sm:
                return i
            i+=1
        return -1
        