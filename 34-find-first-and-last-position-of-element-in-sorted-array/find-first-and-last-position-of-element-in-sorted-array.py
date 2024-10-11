def first_search(nums, target):
    left,right = 0, len(nums)-1
    first_postion = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            first_postion = mid
            right = mid -1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return first_postion

def last_search(nums, target):
    left,right = 0, len(nums)-1
    last_postion = -1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            last_postion = mid
            left = mid+1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return last_postion


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        return [first_search(nums, target), last_search(nums, target)]
        