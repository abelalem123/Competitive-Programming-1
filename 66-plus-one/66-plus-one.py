class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry=1
        n=len(digits)-1
        while n>=0:
            temp=digits[n]+carry
            digits[n]=(temp)%10
            carry=(temp)//10
            if not carry:
                return digits
            n-=1
        res=[]
        if carry:
            res.append(carry)
            return res+digits
        return digits