class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre={0:1}
        sump=0
        res=0
        for i in nums:
            sump+=i
            temp=pre.get(sump%k,0)
            res+=temp
            pre[sump%k]=temp+1
            
        return res    