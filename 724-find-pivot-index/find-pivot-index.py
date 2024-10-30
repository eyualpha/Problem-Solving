class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        sum_ = 0
        total = sum(nums)
        for i,num in enumerate(nums):
            if  sum_ == (total - sum_ - num):
                return i
            sum_ += num
        return -1
            
        