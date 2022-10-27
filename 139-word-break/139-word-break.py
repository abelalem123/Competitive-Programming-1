class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False for _ in range(len(s)+1)]
        dp[len(s)]=True
        for i in range(len(dp)-1,-1,-1):
            for word in wordDict:
                temp=i+len(word)
                if temp<=len(s) and  s[i:temp]==word:
                    dp[i]=dp[temp]
                if dp[i]:
                    break
        return dp[0]
    