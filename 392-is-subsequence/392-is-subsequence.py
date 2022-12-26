class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """
        #if match increase i and j not match increase j
        i=0 1 2 3
        j=0 1 2 3 4 5 6
              i
        s='abc'
                 j
        t='ahbgdc'
        #at the end of loop check if we have reached at len(s) for i True: False 
        """
        s_ind=0
        t_ind=0
        while s_ind<len(s) and t_ind<len(t):
            if s[s_ind]==t[t_ind]:
                s_ind+=1
                t_ind+=1
            else:
                t_ind+=1
        return s_ind==len(s)