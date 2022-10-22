class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        max_count=0
        for i in nums:
            if i-1 not in numset:
                nextn=i
                count=1
                while (nextn+1 in numset):
                    count+=1
                    nextn+=1
                max_count=max(count,max_count)
        return max_count