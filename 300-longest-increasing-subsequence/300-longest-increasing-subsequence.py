class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[-math.inf for i in range(len(nums))] # dp represents the number of sequence upto this interval
        dp[0]=1
        for i in range(1,len(dp)):
            dp[i]=1
            for j in range(0,i):
                if nums[i]>nums[j]:
                    
                    if dp[j]+1>dp[i]:
                        dp[i]=1+dp[j]
        print(dp)
        return max(dp)