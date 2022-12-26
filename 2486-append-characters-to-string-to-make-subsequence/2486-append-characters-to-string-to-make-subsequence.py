class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_ind=0
        t_ind=0
        while s_ind<len(s) and t_ind<len(t):
            if s[s_ind]==t[t_ind]:
                s_ind+=1
                t_ind+=1
            else:
                s_ind+=1
        return len(t)-t_ind