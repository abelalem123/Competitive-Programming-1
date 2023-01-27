class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        left = 0
        right = len(nums)-1
        max_min = 0
        while left<right:
            max_min = max(max_min,nums[left] + nums[right])
            left +=1
            right -=1
        return max_min