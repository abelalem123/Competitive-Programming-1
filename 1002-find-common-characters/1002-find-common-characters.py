class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        comp=list(words[0])
        for i in range(1,len(words)):
            comp=self.common(words[i],comp)
            
        return comp
    def common(self,w1,w2):
        count1=Counter(w1)
        count2=Counter(w2)
        result=[]
        for i in count1:
            if i in count2:
                result.extend(i*min(count1[i],count2[i]))
                    
        return ''.join(result)
        
                