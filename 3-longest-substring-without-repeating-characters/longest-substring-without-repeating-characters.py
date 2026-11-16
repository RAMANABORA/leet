class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        le = 0
        maxle = 0
        st = []
        mpp = {}
        for i in range(len(s)):
            if s[i] in mpp and le <= mpp[s[i]]:
                le = mpp[s[i]]+1
            mpp[s[i]] = i
            maxle = max(maxle,i-le+1) 
        return maxle


        