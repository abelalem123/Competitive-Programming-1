class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        
        
        nums.sort()
        l=0
        max_perimeter=0
        for i in range(2,len(nums)):
            side_sum= nums[i-1] + nums[i-2]
            if side_sum > nums[i]:
                side_sum+=nums[i]
                max_perimeter=max(max_perimeter,side_sum)
        return max_perimeter
                
            