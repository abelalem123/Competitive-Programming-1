class Solution:
    def isHappy(self, n: int) -> bool:
        prev=n
        att=set()
        while True:
            n=self.square_sum(n)
            if n==1:
                return True
            elif n not in att:
                att.add(n)
                continue    
            return False
        #print(self.square_sum(n))
    def square_sum(self,num):
        res=0
        while num>0:
            dig=num%10
            res+=dig**2
            num=num//10
        return res