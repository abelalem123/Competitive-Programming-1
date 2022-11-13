class Solution:
    def sortSentence(self, s: str) -> str:
        # sen=s.split(' ')
        # li=sorted(sen, key=lambda w:w[-1])
        # res=[]
        # for i in li:
        #     res.append(i[:-1])
        # return ' '.join(res)
        
        li=s.split(' ')
        result=['']*len(li)
        for word in li:
            index=int(word[-1])
            result[index-1]=word[:-1]
        return ' '.join(result)