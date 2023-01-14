class Solution:
    def printVertically(self, s: str) -> List[str]:
        words=s.split()
        longest=len(max(words, key=len))
        result=[]
        for i in range(longest):
            temp=[]
            for j in range(len(words)):
                if i<len(words[j]):
                    temp.append(words[j][i])
                else:
                    temp.append(" ")
            #strip trailing space
            while temp[-1]==' ':
                temp.pop()
            result.append(temp)
        ans=[]
        for i in result:
            ans.append(''.join(i))
        return ans