class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        ans=0
        for i,n in enumerate(nums):
            min_val=n
            max_val=n
            for j,n2 in enumerate(nums[i:]):
                min_val=min(min_val,n2)
                max_val=max(max_val,n2)
                ans+= max_val - min_val
        
        return ans