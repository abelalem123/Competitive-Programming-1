class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not len(s):
            return 0
        alph='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        win={i:0 for i in alph}
        #ABAB
        longest=0
        l,r=0,0
        for r in range(len(s)):
            win[s[r]]+=1
            maxc=max(win.values())#this will take o(26)#1
            if k<((r-l+1)-maxc):
                if win[s[l]]!=0:
                    win[s[l]]-=1
                l+=1
            longest=max(r-l+1,longest)
        return longest