class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for i in path.split("/"):
            if i == "" or i == ".":
                pass
            elif i =="..":
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "/"+"/".join(stack)
