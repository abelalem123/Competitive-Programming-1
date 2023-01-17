class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        total=sum(cardPoints)
        length=len(cardPoints)
        win_total,ans,l=0,0,0 #window sum, final answer and left pointer
        for r,n in enumerate(cardPoints):
            win_total+=n
            if r-l+1>length-k:
                win_total-=cardPoints[l]
                l+=1

            if r-l+1==len(cardPoints)-k:
                #our k elements will have a sum of our total minus window sum
                ans=max(ans,total - win_total) 
        return ans