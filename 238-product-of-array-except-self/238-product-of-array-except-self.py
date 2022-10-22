class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        prefix.append(nums[0])
        postfix=[0 for i in range(len(nums))]
        postfix[-1]=nums[-1]
        for i in range(1,len(nums)):
            prefix.append(nums[i]*prefix[i-1])
        for i in range(len(nums)-2,-1,-1):
            postfix[i]=nums[i]*postfix[i+1]
        res=[]
        for idx in range(len(nums)):
            if idx==0:
                res.append(postfix[idx+1])
            elif idx==len(nums)-1:
                res.append(prefix[idx-1])
            else:
                x=prefix[idx-1] * postfix[idx+1]
                res.append(x)
        return res