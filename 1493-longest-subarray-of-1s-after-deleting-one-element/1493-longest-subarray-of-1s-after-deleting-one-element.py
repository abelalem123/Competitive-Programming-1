class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l=0
        longest=0
        win={}
        max_ones=0
        k=1
        for r,n in enumerate(nums):
            win[n]=win.get(n,0)+1
            max_ones=max(max_ones,win.get(1,0))
            while k<(r-l+1)-max_ones:
                win[nums[l]]-=1
                l+=1           
            longest=max(longest,r-l+1)
        return longest-1