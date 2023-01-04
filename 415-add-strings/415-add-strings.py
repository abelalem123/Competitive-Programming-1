class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        
        point_1=len(num1)-1 #pointer to num1
        point_2=len(num2)-1 
        carry=0
        sumn=0
        result=[]
        while point_1 >=0 and point_2>=0:
            sumn=int(num1[point_1]) + int(num2[point_2]) + carry
            carry=sumn//10
            sumn=sumn%10
            point_1-=1
            point_2-=1
            result.append(str(sumn%10))
            #print('here')

        while point_2>=0:
            sumn=int(num2[point_2]) + carry
            carry=sumn//10
            point_2-=1
            result.append(str(sumn%10))
            
        while point_1>=0:
            sumn=int(num1[point_1]) + carry
            carry=sumn//10
            sumn=sumn%10
            point_1-=1
            result.append(str(sumn%10))
            
        if carry:
            #print('here',carry)
            result.append(str(carry))
        
        return ''.join(result[::-1])