class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # sfreq={}
        # tfreq={}
        # for i in s:
        #     sfreq[i]=sfreq.get(i,0)+1
        # for i in t:
        #     tfreq[i]=tfreq.get(i,0)+1
        # for k,v in tfreq.items():
        #     if k not in sfreq or v!=sfreq[k]:
        #         return k
        #bitwise solution
        cup=0
        for i in s:
            cup^=ord(i)
        for i in t:
            cup^=ord(i)
        return chr(cup)