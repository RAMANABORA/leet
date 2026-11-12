class Solution:
    def findUnsortedSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        gt = float('-inf')
        st = float('inf')
        left = right = 0
        for i in range(n):
            if nums[i] >= gt:
                gt = nums[i]
            else:
                right = i
        for i in range(n-1,-1,-1):
            if nums[i] <= st:
                st = nums[i]
            else:
                left = i
        return right - left + 1 if right != 0 or left != 0 else 0


        