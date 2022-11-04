class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited=set()
        l=0
        res=0
        for r in range(len(s)):
            while s[r] in visited:
                visited.remove(s[l])
                l+=1##denotes the number of characters we are deleting
            visited.add(s[r])
            #e.g at r=0, we have found 1 char, hence 0-0+1==1
            res=max(res,r-l+1)                    
        return res        