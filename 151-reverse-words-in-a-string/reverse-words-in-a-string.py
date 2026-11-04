class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip().split()
        ans = ""
        # t = ""
        # res = ""
        # l , r = 0
        # for i in range(len(s)-1,-1,-1):
        #     if s[i] != " ":
        #         t+=s[i]
        #     else:
        #         if t:
        #             res += t[::-1]+" "
        #             t = ""
        # if t:
        #     res += t[::-1]
        # else:
        #     res = res[:-1]
        # return res
        for i in range(len(s)-1,-1,-1):
            ans += s[i]+" "
        return ans.strip()
                

        
