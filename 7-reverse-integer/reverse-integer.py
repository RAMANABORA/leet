class Solution:
    def reverse(self, x: int) -> int:
        r=0
        if(x<0):
            x=abs(x)
            while(x>0):
                d=x%10
                r=r*10+d
                x=x//10
            if(r>(2**31-1)):
                return 0
            else:
                return r*-1
        else:
            while(x>0):
                d=x%10
                r=r*10+d
                x=x//10
            print(r)
            if(r>(2**31-1)):
                return 0
            else:
                return r
            
        

        