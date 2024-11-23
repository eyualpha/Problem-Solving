class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        not_found = True
        for i in words:
            l = 0
            r = len(i)-1
            result = True
            while l<r:
                if i[l] != i[r]:
                    result = False
                l += 1
                r -= 1
            if result:
                return i
                not_found = False
        if not_found:
            return ""
        
        