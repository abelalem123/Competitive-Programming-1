class Solution:
    def freqAlphabets(self, s: str) -> str:
        alph='#abcdefghijklmnopqrstuvwxyz'
        result=[]
        for i in s:
            if i=='#':
                sec=result.pop()
                first=result.pop()
                result.append(first*10+sec)
            else:
                result.append(int(i))
        return ''.join(alph[i] for i in result)
                