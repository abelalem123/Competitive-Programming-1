# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l=1
        r=n
        while l<=r:
            mid=l+(r-l)//2
            q=isBadVersion(mid)
            #print("left",l,"right",r,"mid",mid)
            # if q and (l+1==mid or l==mid):
            #     return l if isBadVersion(l) else mid
            if q:
                r=mid-1
            else:
                l=mid+1
        return l 

    
            