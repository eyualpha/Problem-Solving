class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left,right = 0, len(nums)-1
        
        while left<=right:
            postion = -1
            mid = (left+right)//2
            if nums[mid] == target: 
                postion = mid
                right = mid-1
            elif nums[mid] <target:
                left = mid +1
            else:
                right = mid-1

        if postion == -1:
            return left
        else:
            return postion
      
