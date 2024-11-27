class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        count = 0
        for i in s:
            count += abs(s.index(i) - t.index(i))
        return count
