class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mpp={}
        for i in range(len(strs)):
            l = "".join(sorted(strs[i]))
            if l not in mpp:
                mpp[l] = []
            mpp[l].append(strs[i])
        return list(mpp.values())