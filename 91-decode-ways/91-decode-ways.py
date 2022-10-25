class Solution:
    def numDecodings(self, s: str) -> int:
        dp=[0 for i in range(len(s)+1)]
        dp[0]=1
        if int(s[0]): 
            dp[1]=1
            
        else:
            
            dp[1]=0
        for i in range(2,len(s)+1):
            one=int(s[i-1:i])
            two=int(s[i-2:i])
            print(two)
            if one and 1<=one<=26:
                dp[i]+=dp[i-1]
            if int(s[i-2])!=0 and two<=26:
                dp[i]+=dp[i-2]
        return dp[-1]
                    
                
                