class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        st = []
        stt = []
        for i in range(len(s)):
            if s[i] == "#":
                if st:
                    st.pop()
            else:
                st.append(s[i])
        for i in range(len(t)):
            if t[i] == "#":
                if stt:
                    stt.pop()
            else:
                stt.append(t[i])
        return st == stt
            