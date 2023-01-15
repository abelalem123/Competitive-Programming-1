class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        good={}
        l=0
        num_pairs=0
        result=0
        for r,n in enumerate(nums):
            if n in good:
                good[n]+=1
                num_pairs+=good[n]-1
            else:
                good[n]=1
            
            
            #we have got a sub array, we try to shrink it
            while num_pairs>=k:
                result+=len(nums)-r #given an array [1,1,1] if [1,1] is good so does [1,1,1] 
                good[nums[l]]-=1
                num_pairs-=good[nums[l]]
                l+=1    
        return result
                
            