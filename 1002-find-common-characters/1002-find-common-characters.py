class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        comp=Counter(words[0])
        for i in range(1,len(words)):
            comp&=Counter(words[i])
        return list(comp.elements())
                