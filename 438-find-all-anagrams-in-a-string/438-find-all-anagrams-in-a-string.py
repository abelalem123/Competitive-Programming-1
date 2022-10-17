class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p)>len(s):
            return []
        s1freq=self.count(p)
        start=0
        end=0
        win=self.count(s[:len(p)])
        sol=[]
        if win==s1freq:
            sol.append(0)
        for i in range(len(s)):
            start=s[i]
            try:
                end=s[i+len(p)]
            except:
                return sol
            if win[start]!=0:
                win[start]-=1
            win[end]+=1
            if win==s1freq:
                sol.append(i+1)
        return sol
    def count(self,word:str)->dict:
        alphabets='abcdefghijklmnopqrstuvwxyz'
        alphcount={i:0 for i in alphabets}
        for i in word:
            alphcount[i]+=1
        return alphcount