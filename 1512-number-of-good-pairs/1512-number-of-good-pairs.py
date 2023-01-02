class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1
        sumn=0
        for k,v in count.items():
            if v:
                sumn+=v*(v-1)/2
        return int(sumn)