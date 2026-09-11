class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        c=0
        l=[]
        for i in range(len(nums)):
            c+=nums[i]
            l.append(c)
        return l
