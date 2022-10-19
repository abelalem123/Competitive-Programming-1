class Solution:
    def isHappy(self, n: int) -> bool:
        prev=n
        att={4, 16, 37, 58, 89, 145, 42, 20}
        while True:
            n=self.square_sum(n)
            if n==1:
                return True
            elif n in att:
                return False
            prev=n**2
        #print(self.square_sum(n))
    def square_sum(self,num):
        res=0
        while num>0:
            dig=num%10
            res+=dig**2
            num=num//10
        return res