class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        container= []
        for i in range(len(nums)+1):
            container.append(i)
        if len(nums) == len(container):
            result = (nums[len(nums)-1] +1)
            return result
        else:
            for j in container:
                if j not in nums:
                    return j
            

            
        