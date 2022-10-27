class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False for _ in range(len(s)+1)]
        dp[0]=True
        for i in range(1,len(dp)):
            for word in wordDict:
                temp=i-len(word)
                if temp>=0 and  s[temp:i]==word:
                  
                    dp[i]=dp[temp]
                if dp[i]:
                    break
       
        return dp[-1]
    