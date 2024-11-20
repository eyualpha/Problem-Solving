class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        count = {}
        s = []
        for i in set(nums1):
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in set(nums2):
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in set(nums3):
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
        for i in count:
            if count[i] > 1:
                s.append(i)
        return s   