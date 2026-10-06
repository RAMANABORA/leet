class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        for key,value in freq.items():
            if(value>len(nums)//2):
                return key
        