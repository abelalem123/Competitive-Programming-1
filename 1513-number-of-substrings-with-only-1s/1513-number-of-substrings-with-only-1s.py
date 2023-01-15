class Solution:
    def numSub(self, s: str) -> int:
        ans=0
        count=0
        prev=''
        for n in s:
            if n=='1':
                count+=1
            else:
                count = 0
            ans+=count
            
        return ans % (10**9 + 7)