class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        t = ""
        res = ""
        for i in range(len(s)-1,-1,-1):
            if s[i] != " ":
                t+=s[i]
            else:
                if t:
                    res += t[::-1]+" "
                    t = ""
        if t:
            res += t[::-1]
        else:
            res = res[:-1]
        return res
                

        
