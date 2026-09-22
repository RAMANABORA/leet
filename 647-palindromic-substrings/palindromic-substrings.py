class Solution:
    def expand(self, s:str ,l : int ,r: int)-> int:
        c = 0
        while l>= 0 and r<len(s) and s[l] == s[r]:
            c+=1
            l-=1
            r+=1
        return c
    def countSubstrings(self, s: str) -> int:
        c = 0
        n = len(s)
        for i in range(n):
            c+=self.expand(s , i, i)
            c+= self.expand(s , i , i+1)
        return c
        