class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        cs = 0
        mpp = {0: 1}
        for i in range(len(nums)):
            c += nums[i]
            if c - k in mpp:
                cs += mpp[c - k]
            if c in mpp:
                mpp[c] += 1
            else:
                mpp[c] = 1
        return cs