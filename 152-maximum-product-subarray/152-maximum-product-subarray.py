class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmax=[0 for i in range(len(nums))]
        dpmin=[math.inf for i in range(len(nums))]
        dpmin[0]=nums[0]
        dpmax[0]=nums[0]
        for i in range(1,len(dpmin)):
                dpmax[i]=max(nums[i]*dpmin[i-1],nums[i]*dpmax[i-1],nums[i])
                #print(dpmax[1])
                dpmin[i]=min(nums[i]*dpmin[i-1],nums[i]*dpmax[i-1],nums[i])
                #print(dpmax)
                
        return max(dpmax)