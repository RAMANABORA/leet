class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        ans = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i] , 0)+1
        maxi = max(freq.values())
        for ma in freq.values():
            if ma == maxi:
                ans+=ma
        return ans
        