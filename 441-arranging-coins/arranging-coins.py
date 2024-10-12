class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n

        while left<=right:
            mid = (left+right)//2
            equ = mid*(mid+1)//2
            if equ == n:
                return mid
            elif n > equ:
                left = mid + 1
            else:
                right = mid - 1
        return right
            