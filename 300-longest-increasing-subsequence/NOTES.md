the idea is to have a cache with index 0 to len(nums) indicating the length of the increasing sequence upto that point. init with 1(since each element can be of length one of increasing subsequence)
To answer the question
you iterate through the index at the dp, and for each index you iterate j from 0 up to index-1, basically if nums[j]<nums[i] and the length of the sequence dp[j]+1 is greater than the current dp[i], you assign dp[i]=1+ dp[j].
at last return max of all dp