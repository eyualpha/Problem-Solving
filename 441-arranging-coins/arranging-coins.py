class Solution:
    def arrangeCoins(self, n: int) -> int:
        counter = 0
        i = 1
        while n>=i:
            n -= i
            i += 1
            counter += 1
        return counter