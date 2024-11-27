class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        occur = {0:1}
        counter = 0
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]

            if cur_sum - k in occur:
                counter += occur[cur_sum - k]
            if cur_sum in occur:
                occur[cur_sum] += 1
            else:
                occur[cur_sum] = 1
        return counter