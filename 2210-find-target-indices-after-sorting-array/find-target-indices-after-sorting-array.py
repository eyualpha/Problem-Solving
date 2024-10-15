class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        c = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                c.append(i)
        return c
