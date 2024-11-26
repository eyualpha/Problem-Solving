class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # bruteforce
        # s = []
        # for i in range(len(nums)):
        #     pro = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             pro *= nums[j]
        #     s.append(pro)
        # return s
        
        prefix = [1]*len(nums)
        sufix = [1]*len(nums)

        ans = [0]*len(nums)

        for i in range(1,len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            sufix[i] = nums[i+1]*sufix[i+1]
            
        for i in range(len(nums)):
            ans[i] = prefix[i]*sufix[i]
        
        return ans