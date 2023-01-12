class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        numindex={n:i for i,n in enumerate(nums)}
        result=[0]*len(nums)
        numset=set(nums)
        #print(numset)
        for i,j in operations:
            numindex[j]=numindex[i]
            result[numindex[i]]=j
            del numindex[i]

        for n in numindex:
            result[numindex[n]]=n
        return result