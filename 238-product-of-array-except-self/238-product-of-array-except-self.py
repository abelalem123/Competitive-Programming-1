class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[]
        res.append(1)
        for i in range(1,len(nums)):
                pre=nums[i-1]*res[i-1]
                res.append(pre)
        post=nums[-1]
        for i in range(len(nums)-2,-1,-1):
                res[i]=res[i]*post
                post=post*nums[i]
        return res