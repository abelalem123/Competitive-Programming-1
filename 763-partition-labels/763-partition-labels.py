class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        ababcba
        ab a:1 b:
        """
        remaining=Counter(s)
        win_words=set()
        parts=[]
        l=0
        length=0
        for r,c in enumerate(s):
            win_words.add(c)
            if c in remaining:
                remaining[c]-=1
                if remaining[c]==0:
                    del remaining[c]
            flag=True
            for i in win_words:
                flag=flag and i not in remaining
                    
            if flag: #if our window is unique elements at our window
                parts.append(r-l+1)
                l=r+1
                
        return parts