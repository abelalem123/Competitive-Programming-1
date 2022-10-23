class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return max(nums[0],nums[1])
        # dp excluding first element
        xrob1=nums[1]
        xrob2=max(nums[1],nums[2])
        for i in range(3,len(nums)):
            temp=max(xrob1+nums[i],xrob2)
            xrob1=xrob2
            xrob2=temp
        # dp including first element excluding last element
        rob1=nums[0]
        rob2=max(nums[0],nums[1])
        for i in range(2,len(nums)-1):
            temp=max(rob1+nums[i],rob2)
            rob1=rob2
            rob2=temp
        return max(rob2,xrob2)
  