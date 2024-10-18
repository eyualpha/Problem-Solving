class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = []
        for i in range(len(digits)):
            digits[i] = str(digits[i])
        result = int(''.join(digits)) + 1
        return(list(int(i) for i in str(result)))


        