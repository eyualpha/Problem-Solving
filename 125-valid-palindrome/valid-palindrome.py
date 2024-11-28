class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = "".join(s)
        k = []
        for i in j:
            if i.isalnum():
                k.append(i.lower())
        return k == k[::-1]
        