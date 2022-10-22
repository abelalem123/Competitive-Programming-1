class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset=set(nums)
        starting=set()
        for i in nums:
            if i-1 in numset:
                continue
            else:
                starting.add(i)
        for i in starting:
            numset.remove(i)
        max_count=0
        for i in starting:
            nextn=i+1
            count=1
            while (nextn in numset):
                numset.remove(nextn)
                count+=1
                nextn+=1
            max_count=max(count,max_count)
        return max_count