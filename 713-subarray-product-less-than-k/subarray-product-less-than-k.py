class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        left = 0
        result = 0
        current_product = 1

        for right in range(len(nums)):
            current_product *= nums[right]

            while current_product >= k and left <= right:
                current_product = current_product//nums[left]
                left += 1
            result += (right - left + 1)
        return result
        