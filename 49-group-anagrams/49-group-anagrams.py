class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq=defaultdict(list)
        #word_count=tuple(collections.Counter(strs[0]).items())
        #print(word_count)
        for word in strs:
            count=[0]*26
            for j in word:
                count[ord(j)-ord("a")]+=1
            freq[tuple(count)].append(word)
        return freq.values()
            