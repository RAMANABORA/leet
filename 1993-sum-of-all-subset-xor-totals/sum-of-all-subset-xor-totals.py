class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def solve(st ,x):
            if st == len(nums):
                return x
            a = solve(st+1 , x)
            b = solve(st+1 , x^nums[st])
            return a+b
        
        return solve(0,0)
            

        