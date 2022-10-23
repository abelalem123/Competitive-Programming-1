class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # fi=nums[0]
        # total=0
        # for i in nums:
        #     total+=i
        #     fi=max(total,fi)
        #     if tot
        # res = nums[0]
        # total = 0
        # for n in nums:
        #     total += n
        #     res = max(res, total)
        #     if total < 0:
        #          total = 0
        # return res
        dp=[None for _ in range(len(nums))]
        dp[0]=nums[0]
        for i in range(1,len(nums)):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)