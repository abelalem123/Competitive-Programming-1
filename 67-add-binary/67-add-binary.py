class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res=[]
        i=len(a)-1
        j=len(b)-1
        carry=0
        while i>=0 and j>=0:
            temp=int(a[i]) + int(b[j]) + carry
            carry=temp//2
            res.append(str(temp%2))
            
            i-=1
            j-=1
        while i>=0:
            temp=int(a[i])+carry
            carry=temp//2
            res.append(str(temp%2))
            i-=1
        while j>=0:
            temp=int(b[j])+carry
            carry=temp//2
            res.append(str(temp%2))
            j-=1
        if carry:
            res.append(str(carry))
        res.reverse()
        return ''.join(res)
            