class Solution:
    def maxSumTwoNoOverlap(self, nums: List[int], firstLen: int, secondLen: int) -> int:
        """
        consider two case:
        1. firstlen comes before secondlen maintain max sum of firstlen and move secondlen  as a window
        [0,6,5,2,2,5,1,9,4]
           ____    _ 
        2. firstlen comes after secondlen, so maintain maximum sum of secondlen and move firstlen as a window
        
        [1 2 3 4 5 6]
         - --- 
        """
        firstlen_being_former = self.max_sum(nums,firstLen,secondLen)
        secondlen_being_former = self.max_sum(nums,secondLen,firstLen)
        
        return max(firstlen_being_former, secondlen_being_former)
        
    def max_sum(self,nums,former:int,later:int) -> int:
        
        total_len = former + later 
        former_current_sum = sum(nums[:former])
        later_current_sum = sum(nums[former: total_len])
        former_max_sum =former_current_sum 
        result = former_max_sum + later_current_sum
        
        for i in range(total_len, len(nums)):
            former_current_sum += nums[i-later] - nums[i-total_len]
            later_current_sum += nums[i] - nums[i-later] 
            former_max_sum= max(former_max_sum, former_current_sum)
            result = max(result, former_max_sum + later_current_sum)
            
        return result
            