class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numindex={n:i for i,n in enumerate(nums)}
        result=[0]*len(nums)
        numset=set(nums)
        #print(numset)
        for i,j in operations:
            numset.remove(i)
            numset.add(j)
            numindex[j]=numindex[i]
            result[numindex[i]]=j
        #print(numset)
        for n in numset:
            result[numindex[n]]=n
        return result