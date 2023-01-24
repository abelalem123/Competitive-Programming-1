class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        consider two case:
        1. firstlen comes before secondlen maintain max sum of firstlen and move secondlen  as a window
        [0,6,5,2,2,5,1,9,4]
           _ ___    _ 
        2. firstlen comes after secondlen, so maintain maximum sum of secondlen and move firstlen as a window
        
        [1 2 3 4 5 6]
         - --- 
        """
        
        firstlen_cur = sum(nums[:firstLen])
        secondlen_win = sum(nums[firstLen:firstLen + secondLen])
        left = 0
        firstlen_max = firstlen_cur
        result = firstlen_max + secondlen_win
        #window 1,where we maintain maximum sum of firstlen that appears before secondlen, and we move secondlen as a window
        for i in range(firstLen + secondLen,len(nums)):
            firstlen_cur += nums[i-secondLen] - nums[i-firstLen - secondLen]
            secondlen_win += nums[i] - nums[i-secondLen]
            left+=1
            
            firstlen_max = max(firstlen_max,firstlen_cur)
            result = max(result,firstlen_max + secondlen_win)


        secondlen_cur = sum(nums[:secondLen])
        firstlen_win = sum(nums[secondLen: firstLen + secondLen])
        left = 0
        secondlen_max =secondlen_cur #initialize our sum for secondlen
        
        for i in range(firstLen + secondLen, len(nums)):
            secondlen_cur += nums[i-firstLen] - nums[i-firstLen - secondLen]
            firstlen_win += nums[i] - nums[i-firstLen] 
            left +=1
            secondlen_max= max(secondlen_max, secondlen_cur)
            result = max(result, secondlen_max + firstlen_win)
        return result