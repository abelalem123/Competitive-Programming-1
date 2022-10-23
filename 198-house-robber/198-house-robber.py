class Solution:
    def rob(self, nums: List[int]) -> int:
        maxr=[None for _ in range(len(nums))]
        for idx,i in enumerate(nums):
            if idx==0:
                maxr[0]=i
            elif idx==1:
                maxr[1]=i
            elif idx==2:
                maxr[idx]=maxr[idx-2]+i
            else:
                maxr[idx]=max(maxr[idx-2],maxr[idx-3])+i
        return max(maxr[-1],maxr[-2]) if len(nums)>1 else nums[0]