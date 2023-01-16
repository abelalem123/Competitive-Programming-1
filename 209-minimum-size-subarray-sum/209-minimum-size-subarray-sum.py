class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        [2,3,1,2,4,3]
         that has a sum > target, if i have that i want to see if i can minimize the length even further
        """
        l=0
        min_sub=math.inf
        total = 0
        for r,n in enumerate(nums):
            total +=n
            while total>=target:
                min_sub = min(min_sub,r-l+1)
                total-=nums[l]
                l+=1
        if min_sub==math.inf:
            return 0
        return min_sub
                
            