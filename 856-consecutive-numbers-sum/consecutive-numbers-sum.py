class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        c = 0
        res = 0
        for i in range(1,n+1):
            c += i-1
            if c>=n:
                break
            if (n-c)%i == 0:
                res+=1
        return res
            


        