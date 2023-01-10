class Solution:
    def isPalindrome(self, x: int) -> bool:
        reversed = 0
        n=abs(x)
        while n:
            reversed = reversed*10 + n%10
            n//=10
        return reversed == x