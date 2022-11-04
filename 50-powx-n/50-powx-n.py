class Solution:
    def myPow(self, x: float, n: int) -> float:
        cache
        def pow(x,n):
            if n==0:
                return 1
            if n==1:
                return x
            if n%2==0:
                return pow(x*x,n//2)
            else:
                return x*pow(x*x,n//2)
        res=pow(x,abs(n))
        return res if n==abs(n) else 1/res