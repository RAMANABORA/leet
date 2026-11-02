class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        close =  nums[0] + nums[1] + nums[2]
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                csum = nums[i] + nums[l] + nums[r]
                if abs(csum - target) < abs(close - target):
                    close = csum
                if csum < target:
                    l+=1
                elif csum > target:
                    r-=1
                else :
                    return csum
        return close
        