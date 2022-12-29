class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        #for i in range(len(strs)):
        el=len(strs)
        comp=strs[0]
        for i in range(1,el):
            # find common prefix between the two of them
            comp=self.find_common(comp,strs[i])
            if comp=='':
                break
        return comp

    def find_common(self,s: str, p:str):
        x=min(len(s),len(p))
        result=[]
        for i in range(x):
            if s[i]==p[i]:
                result.append(s[i])
            else:
                break
        return ''.join(result)
                
            