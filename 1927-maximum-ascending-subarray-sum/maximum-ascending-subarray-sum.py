class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        result = []
        s = nums[0]
        if len(nums) == 1:
            return nums[0]
        else:
            for i in range(len(nums)-1):
                if nums[i+1] > nums[i]:
                    s += nums[i+1]
                else:
                    result.append(s)
                    s = nums[i+1]
            result.append(s)    
            return max(result)
        