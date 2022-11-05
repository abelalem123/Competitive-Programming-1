class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=[]
        postfix=[0]*len(nums)
        for i in range(len(nums)-2,-1,-1):
            postfix[i]=postfix[i+1]+nums[i+1]
        for i in range(len(nums)):
            #beginning
            if not i:
                prefix.append(0)
            else:
                prefix.append(prefix[i-1]+nums[i-1])
                
            if postfix[i]==prefix[i]:
                return i

        return -1