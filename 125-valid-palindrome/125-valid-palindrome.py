class Solution:
    def isPalindrome(self, s: str) -> bool:
        lett=[l.lower() for l in s if self.is_alphanum(l)]
        l,r=0,len(lett)-1
        while(r>l):
            if lett[l]!=lett[r]:
                return False
            l+=1
            r-=1
        return True
        
    def is_alphanum(self, letter: chr)->bool:
        return (
            ord('A')<=ord(letter)<=ord('Z') 
            or ord('a')<=ord(letter)<=ord('z') 
            or ord('0')<=ord(letter)<=ord('9')
        )