class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c = []
        for i in nums1:
            if i in nums2:
                c.append(i)
                index = nums2.index(i)
                nums2.pop(index)
        return c
        