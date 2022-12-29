class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        holder={i:j for j,i in enumerate(order)}
        def inorder(first,second):
            min_word=min(len(first),len(second))
            for i in range(min_word):
                if holder[first[i]]<holder[second[i]]:
                    return True
                if holder[first[i]]>holder[second[i]]:
                    return False
            return min_word==len(first)
        comp=words[0]
        for i in range(1,len(words)):
            #compare side by side if it holds continue, else stop and complain
            if inorder(comp,words[i]):
                comp=words[i]
            else:
                return False
        return True

            