class Solution:
    def reverseBits(self, n: int) -> int:
        temp=0
        for i in range(0,32):
            te=(n>>i)&1
            temp=(te<<31-i|temp)
        return temp