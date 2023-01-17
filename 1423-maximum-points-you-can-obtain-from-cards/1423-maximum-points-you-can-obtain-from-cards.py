class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        """
        1 2 3 4 5 6 7 1
        slidding window is len
        """
        total=sum(cardPoints)
        win_total,ans,l=0,0,0
        for r,n in enumerate(cardPoints):
            win_total+=n
            while r-l+1>len(cardPoints)-k:
                win_total-=cardPoints[l]
                l+=1
            if r-l+1==len(cardPoints)-k:
                ans=max(ans,total - win_total)
        return ans