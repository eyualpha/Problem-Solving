class Solution:
    def hammingWeight(self, n: int) -> int:
        x = bin(n)
        y = x[2:]
        count = 0
        for i in y:
            if i == "1":
                count+=1
        return count
        