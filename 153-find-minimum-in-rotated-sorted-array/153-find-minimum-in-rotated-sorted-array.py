class Solution:
    def findMin(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        first=nums[0]
        last=nums[-1]
        if first<=last:#not rotated
            return nums[0]
        while l<=r:
            mid=(l+r)//2
            val=nums[mid]
            print(mid,val)
            if nums[mid-1]>val:# i am near an inflection point
                return val
            #for the rotated arrays
            
            if val>=first:
                l=mid+1
            else:
                r=mid-1
            
                
            