class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        l =0 
        r =len(tokens) -1
        max_score = 0
        score =0
        while l<=r:
            if power >= tokens[l]:
                power -=tokens[l]
                score +=1
                l+=1
                max_score =max(max_score,score)
            elif score >0:
                power +=tokens[r]
                r -=1
                score -=1
                max_score =max(max_score,score)
            else:
                return max_score
            
        return max_score
        # 55 71 82 54 + 84
        # l  r
        