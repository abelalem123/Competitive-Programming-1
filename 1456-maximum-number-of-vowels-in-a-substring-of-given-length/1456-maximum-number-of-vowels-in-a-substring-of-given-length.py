class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        max_vowel = -1
        l =0
        vowels = {'a','e','i','o','u'}
        vowel_buck ={}
        for i in s[:k]:
            if i in vowels:
                vowel_buck[i] = vowel_buck.get(i,0) + 1
            # bucket[i] = bucket.get(i,0) + 1
        max_vowel=sum(vowel_buck.values())
        if max_vowel == k:
            return max_vowel

        for r in range(k,len(s)):
            # if s[l] in bucket:
            #     bucket[s[l]]-=1
            #     if bucket[s[l]]==0:
            #         del bucket[s[l]]
            if s[l] in vowel_buck:
                vowel_buck[s[l]] -=1
                if vowel_buck[s[l]] == 0:
                    del vowel_buck[s[l]]
            
                
            if s[r] in vowels:
                vowel_buck[s[r]] = vowel_buck.get(s[r],0) + 1
            #bucket[s[r]] = bucket.get(i,0) + 1
            
            max_vowel = max(max_vowel, sum(vowel_buck.values()))
            l+=1
        return max_vowel