class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0 
        ps = 0
        seen = {0:1}
        for i in range(len(nums)):
            ps+=nums[i]
            if ps - k in seen:
                c+=seen[ps-k]
            seen[ps] = seen.get(ps,0)+1
        return c
