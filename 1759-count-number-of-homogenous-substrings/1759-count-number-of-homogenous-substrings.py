class Solution:
    def countHomogenous(self, s: str) -> int:
        """

        """
        count={}
        l=0
        ans=0
        prev=''
        for r,c in enumerate(s):
            if c==prev:
                count+=1
            else:
                count=1
                prev=c
            ans+=count
        return ans % (10**9 + 7)
        
        