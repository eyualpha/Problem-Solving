class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        counter = Counter()
        result = 0
        left = 0
        n = len(s)
        for right in range(n):

            counter[s[right]] += 1
            while counter[s[right]] > 2:
                counter[s[left]] -= 1
                left+=1

            result = max(result, right-left+1)
        return result
                    
            
        