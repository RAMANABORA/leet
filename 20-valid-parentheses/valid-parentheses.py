class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i in ")]}":
                if not stack:
                    return False
                top = stack.pop()
                if i == ')' and top != '(':
                    return False
                if i == ']' and top != '[':
                    return False
                if i == '}' and top != '{':
                    return False
        return len(stack) == 0