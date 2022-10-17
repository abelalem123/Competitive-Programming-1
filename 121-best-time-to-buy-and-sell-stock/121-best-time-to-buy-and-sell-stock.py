class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=math.inf
        maxp=0
        for i in range(len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            else:
                maxp=max(prices[i]-buy,maxp)
        return maxp
                