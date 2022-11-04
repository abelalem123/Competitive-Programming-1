class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        li=sorted(nums)
        freq={}
        for idx,i in enumerate(li):
            if i not in freq:
                freq[i]=idx
        res=[]
        for i in nums:
            res.append(freq[i])
        return res