class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        #collect only two types of fruits use map
        # if this map has length >2 decrease it
        l=0
        basket={}
        maxlr=0
        for r,i in enumerate(fruits):
            basket[i]=basket.get(i,0)+1
            while len(basket)>2 and l<=r:
                basket[fruits[l]]-=1
                if basket[fruits[l]]==0:
                    del basket[fruits[l]]
                l+=1
            print(basket)
            maxlr=max(maxlr,r-l+1)
        return maxlr