class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        count, result = 0,0
        is_ok = [0]*len(s)

        for i, e in enumerate(s):
            if e == "(":
                stack.append(i)
            else:
                if stack:
                    is_ok[stack.pop()] = 1
                    is_ok[i] = 1
                else:
                    continue

        for i, e in enumerate(s):
            if is_ok[i] == 1: count += 1
            else: count = 0
            result = max(count, result)
        return result                  
        