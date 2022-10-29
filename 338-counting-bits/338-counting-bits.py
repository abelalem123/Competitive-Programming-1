class Solution:
    def countBits(self, n: int) -> List[int]:
        res=[]
        res.append(0)
        for i in range(1,n+1):
            count=0
            if i%2:
                count+=1
            count+=res[i//2]
            res.append(count)
        return res