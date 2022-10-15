class Solution:
    def hammingWeight(self, n: int) -> int:
        num=0
        for i in range(0,32):
            if (n&(1<<i)):
                num+=1
        return num