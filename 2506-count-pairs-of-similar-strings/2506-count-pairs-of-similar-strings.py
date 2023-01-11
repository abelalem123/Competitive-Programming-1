class Solution:
    def similarPairs(self, words: List[str]) -> int:
        word_set=dict()
        count=0
        for i in words:
            alph=frozenset(i)
            word_set[alph]=word_set.get(alph,0) + 1
        count = 0
        for k,v in word_set.items():
                count =count + v*(v-1)//2
        return count