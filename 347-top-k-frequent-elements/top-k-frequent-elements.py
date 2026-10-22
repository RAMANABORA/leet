class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        ans = []
        for i in range(len(nums)):
            m[nums[i]] = m.get(nums[i] , 0)+1
        sm = sorted(m , key = m.get , reverse = True)
        for j in range(k):
            ans.append(sm[j])
        return ans


        