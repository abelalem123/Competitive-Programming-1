class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #pointers for the two lists given
        p2=len(num2)-1
        sumn=-1
        mult=[]
        while p2>=0:
            result = self.multiply_by_one_digit(num2[p2],num1)
            print(result)
            p2-=1
            if sumn==-1:
                sumn=int(result)
                continue

            power=len(num2)-2-p2
            sumn=int(result)*10**power + sumn   
        return str(sumn)
    
    def multiply_by_one_digit(self,digit,num):
        p1=len(num)-1
        product=deque()
        carry=0
        while p1>=0:
            temp=int(num[p1])*int(digit) + carry
            carry=temp//10
            product.appendleft(str(temp%10))
            p1-=1
        if carry:
             product.appendleft(str(carry))
        return ''.join(product)


        
                