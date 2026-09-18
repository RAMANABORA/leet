class Solution:
    def reverse(self, x: int) -> int:
        n = abs(x)
        res = 0
        while n>0:
            di = n%10
            res = res*10+di
            n = n//10
        if x<0:
            res = -res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
        

        




        