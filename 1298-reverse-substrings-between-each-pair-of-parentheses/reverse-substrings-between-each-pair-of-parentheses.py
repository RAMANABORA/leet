class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        ans = ""
        for ch in s:
            if ch == '(':
                st.append(ans)
                ans = ""
            elif ch == ")":
                ans = ans[::-1]
                ans = st.pop()+ans
            else:
                ans+=ch
        return ans
        