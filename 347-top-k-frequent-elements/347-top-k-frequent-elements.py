class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for i in nums:
            freq[i]=freq.get(i,0)+1
        buck=[[] for i in range(len(nums)+1)]
        for key,value in freq.items():
            buck[value].append(key)
        res=[]
        for i in range(len(buck)-1,0,-1):
            for j in buck[i]:
                res.append(j)
                if len(res)==k:
                    return res