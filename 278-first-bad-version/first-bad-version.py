# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        left, right = 1, n
        postion = 1
        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid):
                postion = mid
                right = mid -1
            else:
                left = mid+1
        return postion
        
           
        