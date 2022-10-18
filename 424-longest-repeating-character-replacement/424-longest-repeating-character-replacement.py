class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not len(s):
            return 0
        longest=0
        l,r=0,0
        maxc=0
        win={}
        for r,ch in enumerate(s):
            win[ch]=1+win.get(ch,0)
            maxc=max(win[ch],maxc)
            while k<((r-l+1)-maxc):
                win[s[l]]-=1
                l+=1
            longest=max(r-l+1,longest)
        return longest