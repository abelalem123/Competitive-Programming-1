class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:

        #slidding window
        #condition to expand the window
        #if k plus sum of elements in the window is greater than 
        #the number at the right times length of the window, why??
        #because it tells us that if all the numbers were all the same as the right
        #the sum would have been just that
        l = 0
        nums.sort()
        total=0
        maxf=0
        for r,n in enumerate(nums):
            #sum of elements in the window
            total+=n
            #condition to shrink the window
            while k+total<n*(r-l+1):
                total-=nums[l]
                l+=1
            maxf=max(maxf,r-l+1)
        return maxf