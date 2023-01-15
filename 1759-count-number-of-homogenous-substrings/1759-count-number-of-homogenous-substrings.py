class Solution:
    def countHomogenous(self, s: str) -> int:
        """

        """
        count={}
        l=0
        ans=0
        for r,c in enumerate(s):
            if c in count:
                count[c]+=1
            else:
                count[c]=1
            
            while len(count)>1:
                count[s[l]]-=1
                if count[s[l]]==0:
                    del count[s[l]]
                l+=1
            ans+=r-l+1
        return ans % (10**9 + 7)
        
        