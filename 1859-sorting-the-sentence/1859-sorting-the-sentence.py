class Solution:
    def sortSentence(self, s: str) -> str:
        sen=s.split(' ')
        li=sorted(sen, key=lambda w:w[-1])
        res=[]
        for i in li:
            res.append(i[:-1])
        return ' '.join(res)