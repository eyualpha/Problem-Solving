class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        start, end = 0, len(nums)-1
        idx = len(nums)-1
        res = [0]*len(nums)

        while idx > -1:
            if abs(nums[start]) < abs(nums[end]):
                res[idx] = nums[end]*nums[end]
                end -= 1
            else:
                res[idx] = nums[start]*nums[start]
                start += 1
            idx -= 1
        return res
        