class Solution:
    def romanToInt(self, s: str) -> int:
        table={'I':1,'V':5,'X':10, 'L':50,'C':100,'D':500,'M':1000}
        res=0
        i=0
        while(i<len(s)):
            if i+1<len(s):
                cur=table[s[i]]
                next=table[s[i+1]]
                if cur>=next:
                    res+=cur
                    i+=1
                else:
                    res+=table[s[i+1]]-table[s[i]]
                    i+=2
            else:
                res+=table[s[i]]
                i+=1
                
        return res