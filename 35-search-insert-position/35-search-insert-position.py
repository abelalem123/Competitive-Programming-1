class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if nums[0]>=target else 1
        l=0
        r=len(nums)-1
        while (l<=r):
            mid=l+(r-l)//2
            val=nums[mid]
            if val==mid:
                return mid
            if l+1==r:
                if val==target:
                    return mid
                if nums[l]>target:
                    return l-1 if l-1!=-1 else 0
                if nums[r]<target:
                    return r+1
                else:
                    return l+1
            elif val<target:
                l=mid
            else:
                r=mid
            
                
                