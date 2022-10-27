class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        l=0
        r=len(nums)-1
        m=-1
        res=[]
        #search for first occurence
        while l<=r:
            mid=l+(r-l)//2
            val=nums[mid]
            if target==val:
                m=mid
                break
            elif target>val:
                l=mid+1
            else:
                r=mid-1
        if m==-1: # not found
            return [-1,-1]
        #search left most index
        l=0
        r=m
        while l<=r:
            mid=l+(r-l)//2
            val=nums[mid]
            if target==val:
                r=mid-1
            elif target>val:
                l=mid+1
            else:
                r=mid-1
        res.append(l)   
        #search right most index
        l=m
        r=len(nums)-1
        while l<=r:
            mid=l+(r-l)//2
            val=nums[mid]
            if target==val:
                l=mid+1
            elif target>val:
                l=mid+1
            else:
                r=mid-1
        res.append(r)
        return res