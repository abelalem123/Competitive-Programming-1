class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=0: return 0
        prod=1
        left=ans=0
        for right,i in enumerate(nums):
            prod*=i
            while prod>=k and left<=right:
                prod/=nums[left]
                left+=1
            ans+=right-left+1
        return ans