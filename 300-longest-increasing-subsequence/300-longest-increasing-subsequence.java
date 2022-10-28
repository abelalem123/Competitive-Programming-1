class Solution {
    public int lengthOfLIS(int[] nums) {
     int[] dp=new int[nums.length];
    dp[0]=1;
    int max_count=1;
    for (int i=1;i<dp.length;i++){
        dp[i]=1;
        for (int j=0;j<i;j++){
            if (nums[i]>nums[j] && dp[j]+1>dp[i]){
                dp[i]=1+dp[j];
                max_count=Math.max(max_count,dp[i]);
            }
        }
    }
    return max_count;
    }
}