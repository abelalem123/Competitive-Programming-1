class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq={}
        count=0
        for i in nums:
            if k-i in freq:
                count+=1
                freq[k-i]-=1
                if freq[k-i]==0:
                    del freq[k-i]
                continue
            freq[i]=freq.get(i,0) + 1
        return count