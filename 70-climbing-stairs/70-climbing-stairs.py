class Solution:
    def __init__(self):
        self.memo={0:0,1:1,2:2}
    def climbStairs(self, n: int) -> int:
        if n<=3:
            return n
        prev,nxt=1,2
        for i in range(4,n+1):
            prev,nxt=nxt,nxt+prev
        return nxt+prev
    def climbrec(self,n:int):
        if n in self.memo:
            return self.memo[n]
        else:
            way1=self.climbStairs(n-1)
            way2=self.climbStairs(n-2)
            self.memo[n]=way1+way2
            return self.memo[n]