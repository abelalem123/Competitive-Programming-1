class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                nums[i]*=2
                nums[i+1]=0
        l=-1
        for i,n in enumerate(nums):
            if n and l!=-1 and l<i:
                nums[l]=n
                nums[i]=0
                l+=1
            if not n and l==-1:
                l=i
        return nums