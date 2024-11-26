class NumArray:

    def __init__(self, nums: List[int]):
        self.acu = [0]+list(accumulate(nums))
        

    def sumRange(self, left: int, right: int) -> int:
        return self.acu[right +1] - self.acu[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)