class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        l = 1
        c = 1
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]:
                continue
            elif nums[i] == nums[i-1]+1:
                c+=1
            else:
                c =1
            l = max(c,l)
        return l
                
                
        