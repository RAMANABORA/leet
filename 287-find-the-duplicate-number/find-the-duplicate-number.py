class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        mpp = {}
        for i in range(len(nums)):
            mpp[nums[i]] = mpp.get(nums[i] , 0)+1
            if mpp[nums[i]]>1:
                return nums[i]

        