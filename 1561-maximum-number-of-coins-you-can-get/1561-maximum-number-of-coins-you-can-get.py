class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        """
        8 7 4 2 2 1
        _____
        """
        piles.sort()
        print(piles)
        total = 0
        left = 0
        right =len(piles)-1
        while left<right:
            left +=1
            right -=1
            total += piles[right]
            right -=1
        return total