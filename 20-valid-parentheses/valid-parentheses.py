class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{","]":"["}

        for i in s:
            if i in mapping:
                if stack and (stack[-1] == mapping[i]):
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        return False
            

