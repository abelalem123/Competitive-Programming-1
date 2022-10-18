class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not len(s):
            return 0
        longest=0
        l,r=0,0
        maxc=0
        win={}
        for r in range(len(s)):
            win[s[r]]=1+win.get(s[r],0)
            maxc=max(win[s[r]],maxc)
            #maxc=max(win.values())#this will take o(26)
            while k<((r-l+1)-maxc):
                win[s[l]]-=1
                l+=1
            longest=max(r-l+1,longest)
        return longest