class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[math.inf for i in range(amount+1)]
        dp[0]=0
        coins.sort()
        for a in range(1,amount+1):
            for c in coins:
                if c>a:
                    break
                dp[a]=min(1+dp[a-c],dp[a])
        if dp[amount]==math.inf:
            return -1
        return  dp[amount]
                