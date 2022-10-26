class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dpmax=[0 for i in range(len(nums))]
        #dpmin=[math.inf for i in range(len(nums))]
        upto_max=1
        upto_min=1
        #dpmin[0]=nums[0]
        #dpmax[0]=nums[0]
        absolute_max=nums[0]
        for num in nums:
                tempmin=num*upto_min
                tempmax=num*upto_max
                upto_max=max(tempmin,tempmax,num)
                upto_min=min(tempmin,tempmax,num)
                absolute_max=max(absolute_max,upto_max)
        return absolute_max