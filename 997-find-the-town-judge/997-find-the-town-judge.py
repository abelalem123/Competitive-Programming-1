class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust and n==1:
            return n
        trusts={}
        trusted={}
        for x,y in trust:
            trusts[x]=y
            trusted[y]=trusted.get(y,0) + 1
        #print(trusted[3])
        for k,v in trusted.items():
            
            if v==(n-1) and k not in trusts:
                return k
        return -1