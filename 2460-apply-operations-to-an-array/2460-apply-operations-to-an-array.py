class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        result=[]
        for i in nums:
            if i:
                result.append(i)
        while len(result)<len(nums):
            result.append(0)
        return result