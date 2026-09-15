class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        cs = 0
        s = str(nums[0])
        for i in range(len(s)):
            freq = [0] * 10

            for n in nums:
                dig = int(str(n)[i])
                freq[dig] += 1
            temp = 0
            for x in freq:
                temp += x * (len(nums)-x)
            cs += temp // 2
                

        return cs