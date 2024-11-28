class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        result = [[],[]]
        for i in nums1:
            if i in nums2:
                continue
            elif i in result[0]:
                continue
            else:
                result[0].append(i)
        for i in nums2:
            if i in nums1:
                continue
            elif i in result[1]:
                continue
            else:
                result[1].append(i)
        return result

        