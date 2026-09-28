class Solution:
    def rotatedDigits(self, n: int) -> int:
        ans = 0
        for i in range(1,n+1):
            c = 0
            valid = True
            changed = False
            curr = i
            while curr>0:
                m = curr%10
                curr = curr//10
                if m in (3,4,7):
                    valid = False
                if m in (2,5,6,9):
                    changed = True
            if valid and changed :
                ans+=1
        return ans

        

        