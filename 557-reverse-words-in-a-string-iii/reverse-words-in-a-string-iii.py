class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split(" ")
        ans=[]
        for i in t:
            ans.append(i[::-1])
        return (" ".join(ans))