class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        c=1
        for i in range(len(nums)):
            if nums[i]==c:
                c+=1
            elif nums[i]<c:
                continue
        return c
        