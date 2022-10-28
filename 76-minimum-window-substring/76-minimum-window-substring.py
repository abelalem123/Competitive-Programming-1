class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        tfreq={}
        
        win={}
        for ch in t:
            tfreq[ch]=tfreq.get(ch,0)+1
        def is_t_in_s(tdict,sdict):
            for t in tdict:
                if t not in sdict:
                    return False
                elif sdict[t]<tdict[t]:
                    return False
            return True
        l=0
        right=0
        right_cand=[]
        min_left=0
        min_right=len(s)
        flag=False
        for r,char in enumerate(s):
            win[char]=1+win.get(char,0)
            while is_t_in_s(tfreq,win):
                flag=True
                if win[s[l]]!=0:
                    win[s[l]]-=1
                else:
                    del win[s[l]]
                l+=1
                if r-l+1<min_right-min_left+1:
                    min_right=r
                    min_left=l
                
        return s[min_left-1:min_right+1] if flag else ''